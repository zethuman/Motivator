from django.contrib import admin

# Register your models here.
from books_module.models import Essay, BookMotivator

admin.site.register(BookMotivator)
admin.site.register(Essay)
