from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from courses_module.models import CourseMotivator
from courses_module.serializers import CourseSerializer, CourseDetailSerializer
from volunteering_module.models import VolunteerMotivator
from volunteering_module.serializers import VolunteerSerializer, VolunteerDetailSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = VolunteerMotivator.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        elif self.action == 'course_detail':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return VolunteerSerializer
        elif self.action == 'create':
            return VolunteerSerializer
        elif self.action == 'update':
            return VolunteerDetailSerializer
        elif self.action == 'destroy':
            return VolunteerDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def course_detail(self, request, pk):
        queryset = VolunteerMotivator.objects.filter(id=pk)
        serializer = VolunteerSerializer(queryset, many=True)
        return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def photo_by_category(request, pk):
#     try:
#         category = Category.objects.get(id=pk)
#     except Category.DoesNotExist as e:
#         return Response({'error': str(e)})
#
#     if request.method == 'GET':
#         serializer = PhotoSerializer(category.photos.all(), many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PhotoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET', 'POST'])
# def comment_by_photo(request, pk):
#     try:
#         photo = Photo.objects.get(id=pk)
#     except Photo.DoesNotExist as e:
#         return Response({'error': str(e)})
#
#     if request.method == 'GET':
#         serializer = CommentSerializer(photo.comments.all(), many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)