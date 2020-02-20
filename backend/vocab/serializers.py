from rest_framework import serializers
#pylint: disable=relative-beyond-top-level
from .models import Vocabs


class VocabsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vocabs
        fields = ("german", "english", "pictureUrl", "picture")