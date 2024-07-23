from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserBio


@receiver(post_save, sender=User)
def create_user_bio(sender, instance, created, **kwargs):
    if created:
        UserBio.objects.create(user=instance)
