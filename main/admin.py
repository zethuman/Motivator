from django.contrib import admin

# Register your models here.
from courses_module.models import CourseMotivator, Content, CertificateForCourse
from main.models import Profile

admin.site.register(Profile)
