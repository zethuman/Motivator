import datetime

from rest_framework import serializers

from books_module.models import BookMotivator, Essay
from courses_module.models import CourseMotivator, Content, Certificate
from volunteering_module.models import VolunteerMotivator, CertificateForVolunteer


class BaseVolunteerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = VolunteerMotivator
        fields = '__all__'
        abstarct = True


class VolunteerSerializer(BaseVolunteerSerializer):

    class Meta:
        model = VolunteerMotivator
        fields = ('id', 'title')


class VolunteerDetailSerializer(BaseVolunteerSerializer):

    class Meta:
        model = VolunteerMotivator
        fields = '__all__'


class BaseCertificateSerializer(serializers.ModelSerializer):
    volunteer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CertificateForVolunteer
        fields = '__all__'
        abstract = True


class VolunteerCertificateSerializer(BaseCertificateSerializer):
    class Meta:
        model = CertificateForVolunteer
        fields = ('id', 'title', 'volunteer_id')


class VolunteerCertificateDetailSerializer(BaseCertificateSerializer):
    class Meta:
        model = CertificateForVolunteer
        fields = '__all__'
