from django.db import models

# Create your models here.
from auth_.models import MainUser


class Points(models.Model):
    points = models.PositiveIntegerField(default=0, verbose_name='Pages')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="points")

    class Meta:
        verbose_name = 'Point'
        verbose_name_plural = 'Points'

    def to_json(self):
        return {
            'id': self.id,
            'points': self.points,
            'user': self.user_id
        }


class Achieves(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='Title')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Description')
    points = models.PositiveIntegerField(default=0, verbose_name='Points')
    reached = models.DateField(blank=True, null=True)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="achieves")

    class Meta:
        verbose_name = 'Achieve'
        verbose_name_plural = 'Achieves'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'user': self.user_id,
        }
