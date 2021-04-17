from rest_framework import serializers

from courses_module.models import CourseMotivator,Content,Certificate,CertificateForCourse


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id','title','description','video','user_id','course_id','is_watched']


class ContentDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only = True)

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
        fields = ('id', 'title', 'course_id')


class CourseCertificateDetailSerializer(BaseCertificateSerializer):
    class Meta:
        model = CertificateForCourse
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    courses_certificate = CourseCertificateSerializer(many = True)

    class Meta:
        model = CourseMotivator
        fields = ('id', 'title', 'status', 'courses_certificate', )


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMotivator
        fields = '__all__'
