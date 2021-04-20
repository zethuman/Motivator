import logging

from django.db.models import F
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.exceptions import PermissionDenied,ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from main.models import Profile
from main.permissions import CurrentUserPermission
from volunteering_module.models import VolunteerMotivator, CertificateForVolunteer
from volunteering_module.serializers import VolunteerSerializer, VolunteerDetailSerializer, VolunteerCertificateDetailSerializer, VolunteerCertificateSerializer


logger = logging.getLogger(__name__)


class VolunteerListAPIView(generics.ListCreateAPIView):
    queryset = VolunteerMotivator.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = (IsAuthenticated,)


class VolunteerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerMotivator.objects.all()
    serializer_class = VolunteerDetailSerializer

    def is_host_user(self,request,*args,**kwargs):
        return self.get_object().user.pk == self.request.user.pk

    def get_permissions(self):
        if self.request.method == 'DELETE':
            permission_classes=(IsAdminUser,)
        else:
            permission_classes=(IsAuthenticated, )

        return [permission() for permission in permission_classes]

    def put(self, request, *args, **kwargs):
        if self.is_host_user(self.request, kwargs=self.kwargs):
            return super().put(request, *args, **kwargs)
        else:
            raise PermissionDenied()


class CertificateViewSet(viewsets.ModelViewSet):

    queryset = CertificateForVolunteer.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (IsAuthenticated,)
        elif self.action == 'certificate_detail_update':
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
            return VolunteerCertificateSerializer
        elif self.action == 'update':
            return VolunteerCertificateDetailSerializer
        elif self.action == 'destroy':
            return VolunteerCertificateDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def certificate_detail_get(self, request, pk, ek):
        queryset = VolunteerMotivator.objects.certificates(pk, ek)
        serializer = VolunteerCertificateDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods = ['POST'], detail = True, permission_classes = (IsAuthenticated,))
    def certificate_create(self, request, pk=None):
        serializer = VolunteerCertificateDetailSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            update_points(uk = request.user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST)

    @action(methods=['PUT'], detail=True, permission_classes=(AllowAny,))
    def certificate_detail_update(self, request, pk, ek):
        queryset = VolunteerMotivator.objects.certificates(pk, ek).first()
        serializer = VolunteerCertificateDetailSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['DELETE'], detail=True, permission_classes=(AllowAny,))
    def certificate_detail_delete(self, request, pk, ek):
        VolunteerMotivator.objects.certificates(pk, ek).first().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def update_points(uk):
    if Profile.objects.get(user_id = uk).points < 30000:
        Profile.objects.filter(user_id = uk).update(points = F('points') + 5000)
        logger.debug(f'Points updated to 5000 user with id: {uk}')
        logger.info(f'Points updated to 5000 user with id: {uk}')
        logger.warning(f'Points updated to 5000 user with id: {uk}')
        logger.error(f'Points updated to 5000 user with id: {uk}')
        logger.critical(f'Points updated to 5000 user with id: {uk}')
    else:
        raise ValidationError("Reached maximum points of 30000")
