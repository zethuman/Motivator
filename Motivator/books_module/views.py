from django.db.migrations import serializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics, status
from rest_framework.response import Response

from books_module.models import BookMotivator, Essay
from books_module.serializers import BookSerializer, EssaySerializer, BookDetailSerializer, EssayDetailSerializer
from courses_module.serializers import ContentSerializer


class BookListAPIView(generics.ListCreateAPIView):
    queryset = BookMotivator.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookMotivator.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (IsAuthenticated, )


class EssayListAPIView(generics.ListCreateAPIView):
    serializer_class = EssaySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Essay.objects.get_by_book(books_id=self.kwargs.get('pk'))
        return queryset


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def essays_by_book(request, pk, ek):
    try:
        essays = BookMotivator.objects.get_essays_in_book(pk, ek)
    except BookMotivator.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = EssayDetailSerializer(essays, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EssayDetailSerializer(essays.first(), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = EssayDetailSerializer(essays.first(), data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        essays.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
