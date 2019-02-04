from django.shortcuts import render
from rest_framework import generics
from .models import Vocabs
from .serializers import VocabsSerializer
from django.http import HttpResponse


class ListVocabsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Vocabs.objects.all()
    serializer_class = VocabsSerializer
    
    def post (self, request, version) :    
        Vocabs.objects.create(german=request.data['german'], english=request.data['english'])
        return HttpResponse("Added new vocab")