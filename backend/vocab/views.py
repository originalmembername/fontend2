from django.shortcuts import render
from rest_framework import generics
from .models import Vocabs
from .serializers import VocabsSerializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
import json


class ListVocabsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Vocabs.objects.all()
    serializer_class = VocabsSerializer
    
    def post (self, request, version) : 
        if Vocabs.objects.filter(german=request.data['german']).count()==0:
            Vocabs.objects.create(german=request.data['german'], english=request.data['english'])
            return JsonResponse({'inserted': 'True'})
        else:
            return JsonResponse({'inserted': 'False'})

    def delete (self, request, version) :
        items = request.data['items']
        if len(items) > 0:
            for vocab in items:
                Vocabs.objects.filter(german=vocab).delete()
            return JsonResponse({ 'deleted' : 'True'})
        else:
            return JsonResponse({ 'deleted' : 'False'})

    def put (self, request, version) :
        key = request.data['germanOld']
        german = request.data['german']
        english = request.data['english']
        if key == german:
            # Only update English
            vocabObj = Vocabs.objects.get(german=key)
            vocabObj.english = english
            vocabObj.save()
            return JsonResponse({ 'edited' : 'True'})
        elif Vocabs.objects.filter(german=german).count()>0:
            #Duplicate
            return JsonResponse({ 'edited' : 'False'})
        else:
            #Update german & english 
            vocabObj = Vocabs.objects.get(german=key)
            vocabObj.german = german
            vocabObj.english = english
            vocabObj.save()
            return JsonResponse({ 'edited' : 'True'})
        