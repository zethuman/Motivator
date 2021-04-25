from django.dispatch import receiver
from django.db.models.signals import post_save

from auth_.models import MainUser
from main.models import Profile


@receiver(post_save, sender=MainUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
