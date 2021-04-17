from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from volunteering_module.models import VolunteerMotivator, CertificateForVolunteer
from volunteering_module.serializers import VolunteerSerializer, VolunteerDetailSerializer, VolunteerCertificateDetailSerializer, VolunteerCertificateSerializer


class VolunteerListAPIView(generics.ListCreateAPIView):
    queryset = VolunteerMotivator.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = (IsAuthenticated,)


class VolunteerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerMotivator.objects.all()
    serializer_class = VolunteerDetailSerializer
    # BookDetailSerializer.is_valid(raise_exception=True)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = CertificateForVolunteer.objects.all()

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
            return VolunteerCertificateSerializer
        elif self.action == 'create':
            return VolunteerCertificateDetailSerializer
        elif self.action == 'update':
            return VolunteerCertificateDetailSerializer
        elif self.action == 'destroy':
            return VolunteerCertificateDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def certificate_detail_get(self, request, pk, ek):
        queryset = VolunteerMotivator.objects.certificates(pk, ek)
        serializer = VolunteerCertificateDetailSerializer(queryset, many=True)
        return Response(serializer.data)

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
