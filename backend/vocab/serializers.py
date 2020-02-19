from rest_framework import serializers
#pylint: disable=relative-beyond-top-level
from .models import Vocabs


class VocabsSerializer(serializers.ModelSerializer):
    picture_url_local = serializers.SerializerMethodField('get_picture_url_local')

    class Meta:
        model = Vocabs
        fields = ("german", "english", "pictureUrl", "picture", "picture_url_local")

    def get_picture_url_local(self, obj):
        return obj.picture.url