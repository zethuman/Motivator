import datetime

from django.db import models
from auth_.models import MainUser
from main.models import BaseModel, Certificate


class CourseMotivatorManager(models.Manager):
    use_in_migrations = True

    # def progress_bar(self, pk):
    #     return self.filter(pages__gt=10).count()


class ContentMotivatorManager(models.Manager):
    use_in_migrations = True


class CourseMotivator(BaseModel):
    deadline = models.DateField(blank=True, null=True, default=datetime.date.today, verbose_name='Deadline')
    status = models.BooleanField(default=False, verbose_name='Status')
    rating = models.FloatField(default=0.0, verbose_name='Rating')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="courses")

    objects = CourseMotivatorManager()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class CertificateForCourse(Certificate):
    course = models.ForeignKey(CourseMotivator, on_delete=models.CASCADE, default=3, related_name="courses_certificate")

    class Meta:
        verbose_name = 'Course certificate'
        verbose_name_plural = 'Course certificates'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }


class Content(BaseModel):
    video = models.CharField(max_length=300, blank=True, default='', verbose_name='Videos')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="contents")
    course = models.ForeignKey(CourseMotivator, on_delete=models.CASCADE, default=3, related_name="courses_content")

    objects = ContentMotivatorManager()

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

