from django.shortcuts import render
from rest_framework import generics
from .models import Vocabs
from .serializers import VocabsSerializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import logging
import requests
from PIL import Image
import requests.exceptions
from io import StringIO
import os
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage


class ListPersonalVocabsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = VocabsSerializer

    def get_queryset(self):
        user = self.request.user
        return user.profile.vocab_list

    # Add-function
    def post(self, request, version):
        profile = self.request.user.profile
        # Check if vocab exists in user's vocab list
        if profile.vocab_list.filter(german=request.data['german']).count() == 0:
            vocab = Vocabs.objects.create(
                german=request.data['german'], english=request.data['english'], pictureUrl=request.data['imgUrl'])
            vocab.save()
            profile.vocab_list.add(vocab)
            return JsonResponse({'inserted': 'True'})
        else:
            return JsonResponse({'inserted': 'False'})

    def delete(self, request, version):
        profile = self.request.user.profile
        items = request.data['items']
        if len(items) > 0:
            for vocab in items:
                profile.vocab_list.filter(german=vocab).delete()
        vocabs = profile.vocab_list
        return JsonResponse({'vocabs': VocabsSerializer(vocabs, many=True).data})

    # Edit-function
    def put(self, request, version):
        profile = self.request.user.profile
        key = request.data['germanOld']
        german = request.data['german']
        english = request.data['english']
        pictureUrl = request.data['imgUrl']
        if key == german:
            # Only update English
            vocabObj = profile.vocab_list.get(german=key)
            vocabObj.english = english
            vocabObj.pictureUrl = pictureUrl
            vocabObj.save()
            return JsonResponse({'edited': 'True'})
        elif profile.vocab_list.filter(german=german).count() > 0:
            # Duplicate
            return JsonResponse({'edited': 'False'})
        else:
            # Update german & english
            vocabObj = profile.vocab_list.get(german=key)
            vocabObj.german = german
            vocabObj.english = english
            vocabObj.pictureUrl = pictureUrl
            vocabObj.save()
            return JsonResponse({'edited': 'True'})


class DownloadException(Exception):
    pass


class DownloadTimeout(DownloadException):
    pass


class DownloadMalformedContentType(DownloadException):
    pass


class DownloadTooBig(DownloadException):
    pass


class ImgTestView(APIView):
    logger = logging.getLogger('uploads')
    MAX_CONTENT_LENGTH = 10485760  # 10mb
    UPLOAD_DIR = 'uploads'
    TIMEOUT = 5  # 5 sec

    def __init__(self, user_pk=None, upload_dir=None, max_content_length=None, timeout=None):
        self.user_pk = user_pk or 'anonymous'
        self.upload_dir = upload_dir or self.UPLOAD_DIR
        self.max_content_length = max_content_length or self.MAX_CONTENT_LENGTH
        self.timeout = timeout or self.TIMEOUT

    def check_content_length(self, response):
        content_length = response.headers.get('content-length', None)
        if not content_length:
            self.logger.error('no content length header')
            raise DownloadMalformedContentType()
        try:
            content_length = int(content_length)
        except ValueError:
            self.logger.error('malformed content type header')
            raise DownloadMalformedContentType()

        if content_length > self.max_content_length:
            self.logger.error(
                'content length too big - {0} bytes'.format(content_length))
            raise DownloadTooBig()

    def post(self, request, version):
        imgUrl = request.data['imgUrl']
        # download image from url
        # get response from url
        try:
            response = requests.get(imgUrl, timeout=self.TIMEOUT, stream=True)
        except requests.exceptions.Timeout:
            self.logger.error("timed out")
            raise DownloadTimeout()
        except requests.exceptions.RequestException as err:
            self.logger.error(err)
            raise DownloadException()
        transfer_encoding = response.headers.get('transfer-encoding', None)
        if transfer_encoding and transfer_encoding.lower() == "chunked":
            self.logger.error('chunked transfer encoding not supported')
            raise DownloadException()
        # check content length
        self.check_content_length(response)

        # get image content
        content = StringIO(response.content)
        try:
            Image.open(content)
        except Exception:
            self.logger.error("can't open content as image")
            raise DownloadException()
        else:
            name = os.path.join(
                self.upload_dir, Storage.generate_filename(self.user_pk, imgUrl))
            storage = FileSystemStorage()
            storage.save(name, ContentFile(content.getvalue()))
            return storage.url(name), storage.path(name)

        # TODO: see https://gist.github.com/FZambia/faab8f811dee95c7b174

        return JsonResponse({'imgUrl': imgUrl})
