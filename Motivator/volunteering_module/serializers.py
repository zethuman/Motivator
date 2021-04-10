import datetime

from rest_framework import serializers

from books_module.models import BookMotivator, Essay
from courses_module.models import CourseMotivator, Content, Certificate
from volunteering_module.models import VolunteerMotivator


class VolunteerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = VolunteerMotivator
        fields = '__all__'


class VolunteerDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = VolunteerMotivator
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Certificate
        fields = '__all__'


class CertificateDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Certificate
        fields = '__all__'
