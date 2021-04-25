import logging
from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.exceptions import ValidationError

from books_module.models import Essay
from courses_module.models import CertificateForCourse
from main.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Essay)
def update_points(sender, instance, created, **kwargs):
    if created:
        if Profile.objects.get(user_id = instance.user.pk).points < 30000:
            Profile.objects.filter(user_id = instance.user.pk).update(points = F('points') + 10000)
            logger.debug(f'Added 10000 points for {instance.book.title} with id {instance.book.id}')
            logger.info(f'Added 10000 points for {instance.book.title} with id {instance.book.id}')
            logger.warning(f'Added 10000 points for {instance.book.title} with id {instance.book.id}')
            logger.error(f'Added 10000 points for {instance.book.title} with id {instance.book.id}')
            logger.critical(f'Added 10000 points for {instance.book.title} with id {instance.book.id}')
        else:
            raise ValidationError("Reached maximum points of 30000")
