from django.contrib import admin

# Register your models here.
from volunteering_module.models import VolunteerMotivator, CertificateForVolunteer

admin.site.register(VolunteerMotivator)
admin.site.register(CertificateForVolunteer)
