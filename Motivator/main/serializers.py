from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.models import Profile
from books_module.models import BookMotivator, Essay


def is_adult_or_old(value):
    age = timezone.now().year - value.year
    if age <= 16 and age <= 63:
        raise serializers.ValidationError('You are not in 16 to 63')


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
        fields = ('id', 'short_bio', 'birth_date', 'points', 'user_id')


class ProfileDetailSerializer(BaseProfileSerializer):

    class Meta(object):
        model = Profile
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(validators=[is_adult_or_old])

    class Meta(object):
        model = Profile
        fields = ['short_bio', 'birth_date', 'rating', 'points',]


class PointsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Profile
        fields = ['points']
