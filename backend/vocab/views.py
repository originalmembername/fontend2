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


class ListPersonalVocabsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    
    serializer_class = VocabsSerializer
    def get_queryset(self):
        user = self.request.user
        return user.profile.vocab_list
    
    #Add-function
    def post (self, request, version) :
        profile = self.request.user.profile
        #Check if vocab exists in user's vocab list
        if profile.vocab_list.filter(german=request.data['german']).count()==0:            
            vocab = Vocabs.objects.create(german=request.data['german'], english=request.data['english'], pictureUrl=request.data['imgUrl'])
            vocab.save()
            profile.vocab_list.add(vocab)
            return JsonResponse({'inserted': 'True'})
        else:
            return JsonResponse({'inserted': 'False'})

    def delete (self, request, version) :
        profile = self.request.user.profile
        items = request.data['items']
        if len(items) > 0:
            for vocab in items:
                profile.vocab_list.filter(german=vocab).delete()
        vocabs = profile.vocab_list
        return JsonResponse({'vocabs' : VocabsSerializer(vocabs, many=True).data})

    #Edit-function
    def put (self, request, version) :
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
            return JsonResponse({ 'edited' : 'True'})
        elif profile.vocab_list.filter(german=german).count()>0:
            #Duplicate
            return JsonResponse({ 'edited' : 'False'})
        else:
            #Update german & english 
            vocabObj = profile.vocab_list.get(german=key)
            vocabObj.german = german
            vocabObj.english = english
            vocabObj.pictureUrl = pictureUrl
            vocabObj.save()
            return JsonResponse({ 'edited' : 'True'})
        
class ImgTestView(APIView):
    def get(self, request, version):
        return JsonResponse({'msg' : 'Image test API'})