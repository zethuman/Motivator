import logging
from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from rest_framework.exceptions import ValidationError
from main.models import Profile
from volunteering_module.models import CertificateForVolunteer

logger = logging.getLogger(__name__)


@receiver(post_save, sender=CertificateForVolunteer)
def update_points(sender, instance, created, **kwargs):
    if created:
        if Profile.objects.get(user_id = instance.user.pk).points < 30000:
            Profile.objects.filter(user_id = instance.user.pk).update(points = F('points') + 5000)
            logger.debug(f'Added 5000 points for {instance.volunteer.title} with id {instance.volunteer.id}')
            logger.info(f'Added 5000 points for {instance.volunteer.title} with id {instance.volunteer.id}')
            logger.warning(f'Added 5000 points for {instance.volunteer.title} with id {instance.volunteer.id}')
            logger.error(f'Added 5000 points for  {instance.volunteer.title} with id {instance.volunteer.id}')
            logger.critical(f'Added 5000 points for  {instance.volunteer.title} with id {instance.volunteer.id}')
        else:
            raise ValidationError("Reached maximum points of 30000")


@receiver(post_delete, sender=CertificateForVolunteer)
def delete_points(sender, instance, *args, **kwargs):
    uk = instance.user.pk
    if Profile.objects.get(user_id = uk).points > 4999:
        Profile.objects.filter(user_id = instance.user.pk).update(points = F('points') - 5000)
        logger.debug(f'Removed 5000 points from {instance.user.first_name} with id {uk}')
        logger.info(f'Removed 5000 points from {instance.user.first_name} with id {uk}')
        logger.warning(f'Removed 5000 points from {instance.user.first_name} with id {uk}')
        logger.error(f'Removed 5000 points from {instance.user.first_name} with id {uk}')
        logger.critical(f'Removed 5000 points from {instance.user.first_name} with id {uk}')
