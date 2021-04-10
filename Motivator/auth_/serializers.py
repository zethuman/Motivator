from rest_framework import serializers

from auth_.models import MainUser


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = MainUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('email', 'password')


