from rest_framework import serializers

from main.models import Points, Achieves
from books_module.models import BookMotivator, Essay


class PointsSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Points
        fields = '__all__'


class AchievesSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Achieves
        fields = '__all__'
