from django.db import models
from django.utils import timezone
from auth_.models import MainUser
from main.models import BaseModel, Certificate


class VolunteerMotivatorManager(models.Manager):
    use_in_migrations = True

    def certificates(self, pk, ek):
        return self.get(id=pk).volunteers_certificates.filter(id=ek)


class VolunteerMotivator(BaseModel):
    start = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='When did it start?')
    end = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='When did it end?')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, null = True,  related_name="volunteers")

    objects = VolunteerMotivatorManager()

    class Meta:
        verbose_name = 'Volunteering'
        verbose_name_plural = 'Volunteering'

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
        }


class CertificateForVolunteer(Certificate):
    volunteer = models.ForeignKey(VolunteerMotivator, on_delete=models.CASCADE, null = True, related_name="volunteers_certificates")
    user = models.ForeignKey(MainUser, on_delete = models.CASCADE, null = True, related_name = 'user_volunteer_certificates')

    class Meta:
        verbose_name = 'Volunteering certificate'
        verbose_name_plural = 'Volunteering certificates'
        unique_together = ('volunteer', 'user')

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }
