import datetime
from django.db import models
from django.utils import timezone

from auth_.models import MainUser
from main.models import BaseModel


class BookMotivatorQuerySet(models.QuerySet):
    use_in_migrations = True

    def get_by_id(self, pk):
        return self.all().get(id=pk)

    def get_essays_in_book(self, pk, ek):
        return self.get_by_id(pk).book_essays.filter(id=ek)


class EssayMotivatorManager(models.Manager):
    use_in_migrations = True

    def get_by_book(self, books_id):
        return self.all().filter(book_id=books_id)


class BookMotivator(BaseModel):
    isbn = models.CharField(max_length=30, blank=True, null=True, verbose_name='ISBN')
    pages = models.PositiveIntegerField(default=0, verbose_name='Pages')
    deadline = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="books")

    objects = BookMotivatorQuerySet().as_manager()

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'pages': self.pages,
            'created': self.created
        }


class Essay(BaseModel):
    essay = models.TextField(max_length=1000, blank=True)
    book = models.ForeignKey(BookMotivator, on_delete=models.CASCADE, null=True, default=3, related_name="book_essays")
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=1, related_name="user_essays")

    objects = EssayMotivatorManager()

    class Meta:
        verbose_name = 'Essay'
        verbose_name_plural = 'Essays'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }
