import datetime

from rest_framework import serializers

from books_module.models import BookMotivator, Essay
from courses_module.models import CourseMotivator, Content, Certificate


class CourseSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CourseMotivator
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CourseMotivator
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class ContentDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Content
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
