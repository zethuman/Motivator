import logging
from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.exceptions import ValidationError
from main.models import Profile
from volunteering_module.models import CertificateForVolunteer

logger = logging.getLogger(__name__)


@receiver(post_save, sender=CertificateForVolunteer)
def update_points(sender, instance, created, **kwargs):
    if created:
        if Profile.objects.get(user_id = instance.user.pk).points < 30000:
            Profile.objects.filter(user_id = instance.user.pk).update(points = F('points') + 5000)
            logger.debug(f'Added 5000 points for course: {instance.volunteer.title} with id {instance.volunteer.id}')
            logger.info(f'Added 5000 points for course: {instance.volunteer.title} with id {instance.volunteer.id}')
            logger.warning(f'Added 5000 points for course: {instance.volunteer.title} with id {instance.volunteer.id}')
            logger.error(f'Added 5000 points for course: {instance.volunteer.title} with id {instance.volunteer.id}')
            logger.critical(f'Added 5000 points for course: {instance.volunteer.title} with id {instance.volunteer.id}')
        else:
            raise ValidationError("Reached maximum points of 30000")
