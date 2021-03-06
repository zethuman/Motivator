import datetime
import logging
from rest_framework import serializers
from books_module.models import BookMotivator, Essay

logger = logging.getLogger(__name__)


def is_13_isbn(value):
    isbn = len(value.replace('-', ''))
    if isbn != 13:
        raise serializers.ValidationError('Please enter 13-digit ISBN')


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    title = serializers.CharField()
    isbn = serializers.CharField(validators=[is_13_isbn])
    pages = serializers.IntegerField()
    deadline = serializers.DateField()
    user_id = serializers.IntegerField(read_only = True)

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
            description=validated_data.get('description'),
            isbn=validated_data.get('isbn'),
            pages=validated_data.get('pages'),
            deadline=validated_data.get('deadline'),
            user_id=self.context['request'].user.id
        )
        return book
        logger.debug(f'Book created ID: {validated_data[id]}')
        logger.info(f'Book created ID: {validated_data[id]}')
        logger.warning(f'Book created ID: {validated_data[id]}')
        logger.error(f'Book created ID: {validated_data[id]}')
        logger.critical(f'Book created ID: {validated_data[id]}')

    def update(self, instance, validated_data):
        pass


class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookMotivator
        fields = '__all__'


class EssaySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    title = serializers.CharField()
    essay = serializers.FileField()
    user_id = serializers.IntegerField(read_only = True)
    book_id = serializers.IntegerField(read_only = True)

    def create(self, validated_data):
        essay = Essay.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            essay=validated_data.get('essay'),
            book_id = self.context['request'].parser_context['kwargs']['pk'],
            user_id=self.context['request'].user.id
        )
        return essay

    def update(self, instance, validated_data):
        pass


class EssayDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Essay
        fields = '__all__'
