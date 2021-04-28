from django.contrib import admin

# Register your models here.
from courses_module.models import CourseMotivator, Content, CertificateForCourse

admin.site.register(CourseMotivator)
admin.site.register(Content)
admin.site.register(CertificateForCourse)
