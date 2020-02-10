from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

image_storage = FileSystemStorage(
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

    picture = models.ImageField(upload_to='media', storage=image_storage, null=True, blank=True)

    class Meta:
        ordering = ('german',)

    def __str__(self):
        return "{} - {}".format(self.german, self.english)
    