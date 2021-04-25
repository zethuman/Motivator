from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from courses_module.serializers import CourseCertificateSerializer,CourseCertificateDetailSerializer
from main.models import Profile
from books_module.models import BookMotivator, Essay


def is_adult_or_old(value):
    age = timezone.now().year - value.year
    if age <= 16 and age <= 63:
        raise serializers.ValidationError('You are not in 16 to 63')


def is_max(value):
    if value >= 30001:
        raise serializers.ValidationError('Reached maximum points, which is 30000')


class BaseProfileSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(validators=[is_adult_or_old, ])
    user_id = serializers.IntegerField(write_only=True)

    class Meta(object):
        model = Profile
        fields = '__all__'
        abstract = True


class ProfileSerializer(BaseProfileSerializer):

    class Meta(object):
        model = Profile
        fields = ('id', 'short_bio', 'birth_date', 'points', 'user')


class ProfileDetailSerializer(BaseProfileSerializer):

    class Meta(object):
        model = Profile
        fields = ('id', 'short_bio', 'birth_date', 'points', 'user', )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(validators=[is_adult_or_old])
    points = serializers.IntegerField(validators = [is_max], read_only = True)

    class Meta(object):
        model = Profile
        fields = ['short_bio', 'birth_date', 'rating', 'points', 'resume', ]
        read_only_fields = ['points', 'rating']


class PointsSerializer(serializers.ModelSerializer):
    points = serializers.IntegerField(validators = [is_max])

    class Meta(object):
        model = Profile
        fields = ['points']
