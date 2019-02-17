from django.db import models

class Vocabs(models.Model):
    # german vocab
    german = models.CharField(max_length=255, null=False, unique=True)
    # english translation
    english = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.german, self.english)
        