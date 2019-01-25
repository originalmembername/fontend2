from django.shortcuts import render
from rest_framework import generics
from .models import Vocabs
from .serializers import VocabsSerializer


class ListVocabsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Vocabs.objects.all()
    serializer_class = VocabsSerializer
