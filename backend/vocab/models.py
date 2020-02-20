import tempfile

import requests
import requests.exceptions
from django.conf import settings
from django.core import files
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.http import HttpResponseNotFound

IMAGE_STORAGE = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/vocab/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}vocab/'.format(settings.MEDIA_URL),
)


class Vocabs(models.Model):

    # german vocab
    german = models.CharField(max_length=255, null=False)
    # english translation
    english = models.CharField(max_length=255, null=False)

    pictureUrl = models.CharField(max_length=255, null=True, default=None)

    picture = models.ImageField(
        upload_to='media', storage=IMAGE_STORAGE, null=True, blank=True)

    class Meta:
        ordering = ('german',)

    @staticmethod
    def create_vocab(german, english, picture_url):
        request = requests.get(picture_url, stream=True)
        # pylint: disable=no-member
        if request.status_code != requests.codes.ok:
            return HttpResponseNotFound(picture_url)
        file_name = picture_url.split('/')[-1]
        temp_file = tempfile.NamedTemporaryFile()
        for block in request.iter_content(1024 * 8):
            if not block:
                break
            temp_file.write(block)

        img_file = files.File(temp_file)
        vocab = Vocabs.objects.create(
            german=german, english=english, pictureUrl=picture_url)
        vocab.picture.save(file_name, img_file)

        return vocab

    def __str__(self):
        return "{} - {}".format(self.german, self.english)
