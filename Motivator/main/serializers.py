from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.models import Profile
from books_module.models import BookMotivator, Essay


# def timer(self):
#     created_on = timezone.now() - self.model('user_id').created_at
#     print("Now", timezone.now().day)
#     print("Created date", self.model('user_id').created_at.day)
#     print("Created date on days", created_on.days)
#
#     if created_on.days >= 0:
#         set_max_value(30000)
#         print(3000)
#     pass
#
#
# def set_max_value(value):
#     return 30000 + value;

#
# def time_to_update(value):
#     if value > set_max_value(0):
#         raise ValidationError(
#             ('You reached max points in this quartal'),
#             params={'value': value},
#         )
#

class ProfileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Profile
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Profile
        fields = ['short_bio', 'birth_date', 'rating', 'points',]


class PointsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Profile
        fields = ['points']
