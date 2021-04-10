import datetime

from django.db.models import F
from rest_framework import serializers

from books_module.models import BookMotivator, Essay
from main.models import Profile


def is_13_isbn(value):
    isbn = len(value.replace('-', ''))
    if isbn != 13:
        raise serializers.ValidationError('Please enter 13-digit ISBN')


def add_points(self):
    Profile.objects.filter(user_id=self.data['user_id']).update(points=F('points') + 10000)


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    isbn = serializers.CharField(validators=[is_13_isbn])
    pages = serializers.IntegerField()
    created = serializers.DateTimeField(read_only=True)
    deadline = serializers.DateField()
    user_id = serializers.IntegerField(write_only=True)

    def validate_pages(self, value):
        if value >= 2000 or value <= 0:
            raise serializers.ValidationError("A book cannot have more than 2000 pages and less than 1 page")
        else:
            return value

    def validate(self, data):
        if datetime.date.today() >= data['deadline']:
            raise serializers.ValidationError("Deadline must be more than 1 day")
        return data

    def create(self, validated_data):
        book = BookMotivator.objects.create(
            title=validated_data.get('title'),
            isbn=validated_data.get('isbn'),
            pages=validated_data.get('pages'),
            deadline=validated_data.get('deadline'),
            user_id=validated_data.get('user_id')
        )
        return book

    def update(self, instance, validated_data):
        pass


class BookDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BookMotivator
        fields = '__all__'


class EssaySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    essay = serializers.CharField()
    books_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        add_points(self)
        essay = Essay.objects.create(
            title=validated_data.get('title'),
            essay=validated_data.get('essay'),
            books_id=validated_data.get('books_id'),
            user_id=validated_data.get('user_id')
        )
        return essay

    def update(self, instance, validated_data):
        pass


class EssayDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    books_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Essay
        fields = '__all__'
