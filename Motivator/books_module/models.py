import datetime
from django.db import models
from auth_.models import MainUser
from main.models import BaseModel


class BookMotivatorManager(models.Manager):
    use_in_migrations = True

    def duration(self):
        return datetime.datetime.now() - self.created


class EssayMotivatorManager(models.Manager):
    use_in_migrations = True


class BookMotivator(BaseModel):
    isbn = models.CharField(max_length=30, blank=True, null=True, verbose_name='ISBN')
    pages = models.PositiveIntegerField(default=0, verbose_name='Pages')
    deadline = models.DateField(blank=True, null=True, default=datetime.date.today)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="books")

    objects = BookMotivatorManager()

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
    books = models.ForeignKey(BookMotivator, on_delete=models.CASCADE, null=True, default=3, related_name="books")
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, default=3, related_name="essays")

    objects = EssayMotivatorManager()

    class Meta:
        verbose_name = 'Essay'
        verbose_name_plural = 'Essays'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'user': self.user_id,
            'book': self.books_id
        }
