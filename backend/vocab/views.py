import json
import logging
import os
import sys
import tempfile
from io import StringIO
from django.core.files.storage import default_storage

import requests
import requests.exceptions
from django.core import files, serializers
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage, Storage
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from PIL import Image
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

#pylint: disable=relative-beyond-top-level
from .models import Vocabs
from .serializers import VocabsSerializer


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


class ImgTestView(APIView):

    def post(self, clientRequest, version):
        imgUrl = clientRequest.data['imgUrl']
        # Steam the image from the url
        request = requests.get(imgUrl, stream=True)
        # Was the request OK?
        # pylint: disable=no-member
        if request.status_code != requests.codes.ok:
            # Nope, error handling, skip file etc etc etc
            return HttpResponseNotFound(imgUrl)
        # Get the filename from the url, used for saving later
        file_name = imgUrl.split('/')[-1]
        # Create a temporary file
        lf = tempfile.NamedTemporaryFile()
        # Read the streamed image in sections
        for block in request.iter_content(1024 * 8):
            # If no more file then stop
            if not block:
                break
            # Write image block to temporary file
            lf.write(block)

        #TODO:Remove     Save img to file system
        imgFile = files.File(lf)

        # Create the model you want to save the image to
        vocab = Vocabs.objects.create(
                german='neueVokabel', english='newVocab', pictureUrl=imgUrl)

        # Save the temporary image to the model#
        # This saves the model so be sure that is it valid
        vocab.picture.save(file_name, imgFile)

        return JsonResponse({'imgUrl': imgUrl})
