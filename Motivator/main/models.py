from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.db import models
# Create your models here.
from django.utils import timezone
from auth_.models import MainUser


class BaseModel(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='Title')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Description')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Base'
        verbose_name_plural = 'Bases'
        abstract = True

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }


class Certificate(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='Title')
    number = models.CharField(max_length=100, blank=True, null=True, verbose_name='Certificate number')
    file = models.FileField(upload_to = 'certificates', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'jpg', 'png', 'jpeg'])
    ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
        abstract = True

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }


class Profile(models.Model):
    short_bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True, default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to = 'resumes', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc'])
    ])
    rating = models.FloatField(default=0.0, validators=[MaxValueValidator(5.0, message="Rating can't be more than 5"), ] ,verbose_name='Rating')
    points = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(30000, message="Reached maximum points for this quartal")], verbose_name='Points')
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user

    def to_json(self):
        return {
            'id': self.id,
            'bio': self.short_bio,
            'rating': self.rating,
            'points': self.points
        }
