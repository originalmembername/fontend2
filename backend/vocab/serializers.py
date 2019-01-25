from rest_framework import serializers
from .models import Vocabs


class VocabsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabs
        fields = ("german", "english")