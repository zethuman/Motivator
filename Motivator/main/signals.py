import logging
import os
import shutil

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete

from main.models import Profile


@receiver(post_delete, sender=Profile)
def delete_resume_on_profile_delete(sender, instance, *args, **kwargs):
    resume = instance.resume
    if resume:
        user_resume_path = os.path.abspath(os.path.join(resume.path, '../..'))
        shutil.rmtree(user_resume_path)

