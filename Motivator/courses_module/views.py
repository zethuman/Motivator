from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.response import Response

from courses_module.models import CourseMotivator,Content,CertificateForCourse
from courses_module.serializers import CourseSerializer,CourseDetailSerializer,ContentSerializer, \
    ContentDetailSerializer,CourseCertificateDetailSerializer, \
    CourseCertificateSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = CourseMotivator.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes=(IsAuthenticated,)
        elif self.action == 'create':
            permission_classes=(IsAuthenticated,)
        elif self.action == 'update':
            permission_classes=(IsAuthenticated,)
        elif self.action == 'destroy':
            permission_classes=(IsAdminUser,)
        else:
            permission_classes=(IsAuthenticated, )

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseSerializer
        elif self.action == 'create':
            return CourseSerializer
        elif self.action == 'update':
            return CourseDetailSerializer
        elif self.action == 'destroy':
            return CourseDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(IsAuthenticated,))
    def course_detail(self, request, pk):
        queryset = CourseMotivator.objects.details(pk)
        serializer = CourseDetailSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def list_contents_by_course(request, pk):
    try:
        course = CourseMotivator.objects.get(id=pk)
    except Content.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = ContentSerializer(course.courses_content.all(), many=True)
        return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes((IsAdminUser, ))
# def list_contents_by_course(request):
#     if request.method == 'POST':
#         serializer = ContentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def content_by_course(request, pk, ek):
    try:
        contents = CourseMotivator.objects.get_contents_in_course(pk, ek)
    except CourseMotivator.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = ContentDetailSerializer(contents, many=True)

        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ContentDetailSerializer(contents.first(), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ContentDetailSerializer(contents.first(), data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contents.first().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = CertificateForCourse.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (IsAuthenticated,)
        elif self.action == 'create':
            permission_classes = (IsAuthenticated,)
        elif self.action == 'update':
            permission_classes = (IsAuthenticated,)
        elif self.action == 'destroy':
            permission_classes = (IsAdminUser,)
        elif self.action == 'certificate_detail_delete':
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseCertificateSerializer
        elif self.action == 'create':
            return CourseCertificateDetailSerializer
        elif self.action == 'update':
            return CourseCertificateDetailSerializer
        elif self.action == 'destroy':
            return CourseCertificateDetailSerializer


    @action(methods=['GET'], detail=True, permission_classes=(IsAuthenticated,))
    def certificate_detail_get(self, request, pk, ek):
        queryset = CourseMotivator.objects.certificates(pk, ek)
        serializer = CourseCertificateDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['PUT'], detail=True, permission_classes=(IsAuthenticated,))
    def certificate_detail_update(self, request, pk, ek):
        queryset = CourseMotivator.objects.certificates(pk, ek).first()
        serializer = CourseCertificateDetailSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['DELETE'], detail=True, permission_classes=(IsAdminUser,))
    def certificate_detail_delete(self, request, pk, ek):
        CourseMotivator.objects.certificates(pk, ek).first().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
