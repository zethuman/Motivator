from django.db.migrations import serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from books_module.models import BookMotivator, Essay
from books_module.serializers import BookSerializer, EssaySerializer, BookDetailSerializer, EssayDetailSerializer


class BookListAPIView(generics.ListCreateAPIView):
    queryset = BookMotivator.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookMotivator.objects.all()
    serializer_class = BookDetailSerializer
    # BookDetailSerializer.is_valid(raise_exception=True)


class EssayListAPIView(generics.ListCreateAPIView):
    serializer_class = EssaySerializer
    # EssaySerializer.is_valid(raise_exception=True)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Essay.objects.all().filter(books_id=self.kwargs.get('pk'))
        return queryset


class EssayDetailAPIView(generics.ListCreateAPIView):
    serializer_class = EssayDetailSerializer
    # EssayDetailSerializer.is_valid(raise_exception=True)

    def get_queryset(self):
        queryset = Essay.objects.all().filter(books_id=self.kwargs.get('pk')).filter(id=self.kwargs.get('ek'))
        return queryset
