from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from vocab.models import Vocabs

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    past_lessons = models.IntegerField(blank=True, default=0)
    upcoming_lessons = models.IntegerField(blank=True, default=0)
    protocol_url = models.CharField(max_length=300, blank=True)
    folder_url = models.CharField(max_length=300, blank=True)
    vocab_list = models.ManyToManyField(Vocabs)

    def __str__(self):
        return "{}  {} from {}".format(self.user.first_name, self.user.last_name, self.location)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
