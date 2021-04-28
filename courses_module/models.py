import datetime

from django.core.validators import MaxValueValidator
from django.db import models
from auth_.models import MainUser
from main.models import BaseModel, Certificate


class CourseMotivatorQuerySet(models.QuerySet):
    use_in_migrations = True

    def find_course_by_title(self, title):
        return self.filter(title__contains=title)

    def sort_by_rating(self):
        return self.order_by('rating')

    def get_not_passed(self):
        return self.filter(status=False)

    def details(self, pk):
        return self.filter(id=pk)

    def get_by_id(self, pk):
        return self.all().get(id=pk)

    def get_contents_in_course(self, pk, ek):
        return self.get_by_id(pk).courses_content.filter(id=ek)

    def certificates(self, pk, ek):
        return self.get(id=pk).courses_certificate.filter(id=ek)

    def my_certificates(self, pk, ek, uk):
        return self.certificates(pk, ek).get(user_id = uk)


class ContentMotivatorManager(models.Manager):
    use_in_migrations = True


class CourseMotivator(BaseModel):
    deadline = models.DateField(blank=True, null=True, default=datetime.date.today, verbose_name='Deadline')
    status = models.BooleanField(default=False, verbose_name='Status')
    rating = models.FloatField(default=0.0, verbose_name='Rating', validators=[MaxValueValidator(5.0), ])
    user = models.ManyToManyField(MainUser, related_name='courses')

    objects = CourseMotivatorQuerySet().as_manager()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class CertificateForCourse(Certificate):
    course = models.ForeignKey(CourseMotivator, on_delete=models.CASCADE, related_name="courses_certificate")
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, null = True, related_name = 'user_course_certificates')

    class Meta:
        verbose_name = 'Course certificate'
        verbose_name_plural = 'Course certificates'
        unique_together = ('course', 'user')

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }


class Content(BaseModel):
    video = models.CharField(max_length=300, blank=True, default='', verbose_name='Videos')
    user = models.ManyToManyField(MainUser, related_name="contents")
    course = models.ForeignKey(CourseMotivator, on_delete=models.CASCADE, default=1, related_name="courses_content")

    objects = ContentMotivatorManager()

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

