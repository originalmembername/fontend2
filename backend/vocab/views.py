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

    """ def delete (self, request, version) :
         """