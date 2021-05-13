import logging
import os
import shutil

from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from rest_framework.exceptions import ValidationError

from Motivator import settings
from books_module.models import Essay
from courses_module.models import CertificateForCourse
from main.models import Profile


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Essay)
def update_points(sender, instance, created, **kwargs):
    if created:
        if Profile.objects.get(user_id = instance.user.pk).points < 30000:
            Profile.objects.filter(user_id = instance.user.pk).update(points = F('points') + 5000)
            logger.debug(f'Added 5000 points for {instance.book.title} with id {instance.book.id}')
            logger.info(f'Added 5000 points for {instance.book.title} with id {instance.book.id}')
            logger.warning(f'Added 5000 points for {instance.book.title} with id {instance.book.id}')
            logger.error(f'Added 5000 points for {instance.book.title} with id {instance.book.id}')
            logger.critical(f'Added 5000 points for {instance.book.title} with id {instance.book.id}')
        else:
            raise ValidationError("Reached maximum points of 30000")


@receiver(post_delete, sender=Essay)
def delete_points(sender, instance, *args, **kwargs):
    uk = instance.user.pk
    if Profile.objects.get(user_id = uk).points > 4999:
        Profile.objects.filter(user_id = instance.user.pk).update(points = F('points') - 5000)


@receiver(post_delete, sender=Essay)
def delete_essays_on_book_delete(sender, instance, *args, **kwargs):
    essay = instance.essay
    if essay:
        # essay_path = os.path.join(settings.MEDIA_ROOT, essay)
        os.remove(essay.path)
