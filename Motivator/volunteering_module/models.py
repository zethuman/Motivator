from django.db import models
import datetime
from auth_.models import MainUser
from main.models import BaseModel, Certificate


class VolunteerMotivatorManager(models.Manager):
    use_in_migrations = True

    # def progress_bar(self, pk):
    #     return self.filter(pages__gt=10).count()


class CertificateManager(models.Manager):
    use_in_migrations = True


class VolunteerMotivator(BaseModel):
    start = models.DateField(blank=True, null=True, default=datetime.date.today, verbose_name='When did it start?')
    end = models.DateField(blank=True, null=True, default=datetime.date.today, verbose_name='When did it end?')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="volunteers")

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
    volunteer = models.ForeignKey(VolunteerMotivator, on_delete=models.CASCADE, default=3, related_name="volunteers_certificates")

    objects = CertificateManager()

    class Meta:
        verbose_name = 'Volunteering certificate'
        verbose_name_plural = 'Volunteering certificates'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }
