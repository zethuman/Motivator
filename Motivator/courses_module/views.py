import logging

from django.db.models import F
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.exceptions import ValidationError,MethodNotAllowed
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.response import Response

from courses_module.models import CourseMotivator,Content,CertificateForCourse
from courses_module.serializers import CourseSerializer,CourseDetailSerializer,ContentSerializer, \
    ContentDetailSerializer,CourseCertificateDetailSerializer, \
    CourseCertificateSerializer
from main.models import Profile
from main.permissions import AdminPermission,HrPermission,MyCustomPermission
from django.forms.models import model_to_dict

logger = logging.getLogger(__name__)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = CourseMotivator.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes=(IsAuthenticated,)
        elif self.action == 'create':
            permission_classes=(IsAdminUser,)
        elif self.action == 'update':
            permission_classes=(IsAdminUser,)
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


@api_view(['GET', 'POST'])
@permission_classes([MyCustomPermission])
def list_contents_by_course(request, pk):
    try:
        course = CourseMotivator.objects.get(id=pk)
    except Content.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = ContentSerializer(course.courses_content.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'Content created ID: {serializer.instance}')
            logger.info(f'Content created ID:  {serializer.instance}')
            logger.warning(f'Content created ID:  {serializer.instance}')
            logger.error(f'Content created ID:  {serializer.instance}')
            logger.critical(f'Content created ID:  {serializer.instance}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([MyCustomPermission])
def content_by_course(request, pk, ek):
    try:
        contents = CourseMotivator.objects.get_contents_in_course(pk, ek)
    except CourseMotivator.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = ContentDetailSerializer(contents, many=True)
        Content.objects.get(id=ek).user.add(request.user.id)
        if CourseMotivator.objects.get(id=pk).courses_content.count() == CourseMotivator.objects.get(id = pk).courses_content.filter(user = request.user.id).count():
            queryset = CertificateForCourse.objects.filter(course_id = pk)
            if queryset.filter(user_id = request.user.id).exists():
                return Response(serializer.data)
            else:
                post_certificate(pk,request.user.id)
                update_points(uk = request.user.id)
                return Response(serializer.data)
        else:
            return Response(serializer.data)
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


def post_certificate(pk, uk):
    title = f'Certificate for {CourseMotivator.objects.get(id=pk).title}'
    number = "123456789"
    course_id = pk
    user_id = uk
    CertificateForCourse.objects.create(title=title, number=number, course_id=course_id, user_id=user_id)
    logger.debug(f'Certificate for course {course_id} created ID')
    logger.info(f'Certificate for course {course_id} created ID')
    logger.warning(f'Certificate for course {course_id} created ID')
    logger.error(f'Certificate for course {course_id} created ID')
    logger.critical(f'Certificate for course {course_id} created ID')


def update_points(uk):
    if Profile.objects.get(user_id = uk).points < 30000:
        Profile.objects.filter(user_id = uk).update(points = F('points') + 10000)
    else:
        raise ValidationError("Reached maximum points of 30000")


class CertificateViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = CertificateForCourse.objects.filter(user = self.request.user.id)
        return queryset

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (IsAuthenticated,)
        elif self.action == 'create':
            permission_classes = (IsAdminUser,)
        elif self.action == 'update':
            permission_classes = (IsAdminUser,)
        elif self.action == 'destroy':
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseCertificateSerializer
        elif self.action == 'create':
            return CourseCertificateDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(IsAuthenticated,))
    def certificate_detail_get(self, request, pk, ek):
        queryset = CourseMotivator.objects.certificates(pk, ek)
        serializer = CourseCertificateDetailSerializer(queryset.filter(user = request.user.id), many=True)
        return Response(serializer.data)

    @action(methods=['PUT'], detail=True, permission_classes=(IsAdminUser,))
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
