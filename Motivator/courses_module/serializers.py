from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from courses_module.models import CourseMotivator,Content,Certificate,CertificateForCourse


class ContentSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only = True)

    class Meta:
        model = Content
        fields = ['id', 'title', 'description', 'video', 'course_id', ]


class ContentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class BaseCertificateSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CertificateForCourse
        fields = '__all__'
        abstract = True


class CourseCertificateSerializer(BaseCertificateSerializer):
    class Meta:
        model = CertificateForCourse
        fields = ('id', 'title', 'course')


class CourseCertificateDetailSerializer(BaseCertificateSerializer):
    created = serializers.DateTimeField(read_only = True)
    updated = serializers.DateTimeField(read_only = True)

    class Meta:
        model = CertificateForCourse
        fields = ('id', 'course_id', 'title', 'number', 'file', 'created', 'updated')


class CourseSerializer(serializers.ModelSerializer):
    courses_content = ContentSerializer(many = True, read_only = True)
    # courses_certificate = CourseCertificateSerializer(many = True, read_only = True)

    class Meta:
        model = CourseMotivator
        fields = ('id', 'title', 'status', 'courses_content', )


class CourseDetailSerializer(serializers.ModelSerializer):
    courses_content = ContentDetailSerializer(many = True, read_only = True)
    # courses_certificate = CourseCertificateDetailSerializer(many = True,read_only = True)

    class Meta:
        model = CourseMotivator
        fields = ('id', 'title', 'status', 'description', 'created', 'updated', 'deadline', 'rating',  'courses_content',)
