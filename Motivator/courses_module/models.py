import datetime

from django.db import models
from auth_.models import MainUser


class CourseMotivatorManager(models.Manager):
    use_in_migrations = True

    # def progress_bar(self, pk):
    #     return self.filter(pages__gt=10).count()


class ContentMotivatorManager(models.Manager):
    use_in_migrations = True


class BaseModel(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='Title')
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Description')

    class Meta:
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


class CourseMotivator(BaseModel):
    deadline = models.DateField(blank=True, null=True, default=datetime.date.today)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="courses")

    objects = CourseMotivatorManager()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Content(BaseModel):
    video = models.FileField()
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="contents")

    objects = ContentMotivatorManager()

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'


class Certificate(BaseModel):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="certificates")

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
