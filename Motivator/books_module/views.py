from django.core.exceptions import SuspiciousOperation
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser,JSONParser,MultiPartParser
from books_module.models import BookMotivator, Essay
from books_module.serializers import BookSerializer, EssaySerializer, BookDetailSerializer, EssayDetailSerializer
from main.permissions import HrPermission, AdminPermission


class BookListAPIView(generics.ListCreateAPIView):
    queryset = BookMotivator.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class MyBookListAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = BookMotivator.objects.filter(user_id = self.request.user.id)
        return queryset


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookMotivator.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (IsAuthenticated, )

    def is_host_user(self, request, *args, **kwargs):
        return self.get_object().user.pk == self.request.user.pk

    def delete(self, request, *args, **kwargs):
        if self.is_host_user(request=self.request, kwargs=self.kwargs) or AdminPermission:
            return super().delete(request, *args, **kwargs)
        else:
            raise PermissionDenied()


class EssayListAPIView(generics.ListCreateAPIView):
    serializer_class = EssaySerializer
    permission_classes = (HrPermission,)
    parser_classes = [FormParser,MultiPartParser,JSONParser]

    def get_queryset(self):
        queryset = Essay.objects.get_by_book(books_id=self.kwargs.get('pk'))
        return queryset


class MyEssayListAPIView(generics.ListCreateAPIView):
    serializer_class = EssaySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Essay.objects.get_by_book_by_user(user_id = self.request.user.id, books_id=self.kwargs.get('pk'))
        return queryset


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([HrPermission])
@parser_classes([FormParser, MultiPartParser, JSONParser])
def essays_by_book(request, pk, ek):
    try:
        essays = BookMotivator.objects.get_essays_in_book(pk, ek)
    except BookMotivator.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = EssayDetailSerializer(essays, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT' and BookMotivator.objects.get(id=pk).user.pk == request.user.pk:
        serializer = EssayDetailSerializer(essays.first(), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH' and BookMotivator.objects.get(id=pk).user.pk == request.user.pk:
        serializer = EssayDetailSerializer(essays.first(), data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        essays.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        raise SuspiciousOperation
