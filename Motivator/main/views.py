from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from main.models import Profile
from main.serializers import ProfileSerializer, PointsSerializer, ProfileUpdateSerializer, ProfileDetailSerializer


class ProfileViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    queryset = Profile.objects.all()

    def is_host_user(self, request, *args, **kwargs):
        return self.get_object().user.pk == self.request.user.pk

    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileSerializer
        elif self.action == 'create':
            return ProfileSerializer
        elif self.action == 'update':
            return ProfileUpdateSerializer
        elif self.action == 'destroy':
            return ProfileSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes=(IsAuthenticated,)
        elif self.action == 'create':
            permission_classes=(IsAuthenticated,)
        elif self.action == 'update':
            permission_classes=(IsAuthenticated,)
        elif self.action == 'destroy':
            permission_classes=(IsAdminUser,)
        elif self.action == 'nullify':
            permission_classes=(IsAdminUser,)
        else:
            permission_classes=(IsAuthenticated,)

        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        if self.is_host_user(self.request, kwargs=self.kwargs):
            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    @action(methods=['GET'], detail=True, permission_classes=(IsAuthenticated,))
    def profile_detail(self, request, pk):
        queryset = Profile.objects.filter(id=pk)
        serializer = ProfileDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['PUT'], detail=False, permission_classes=(IsAdminUser,))
    def nullify(self, request):
        queryset = Profile.objects.update(points=0)
        serializer = PointsSerializer(queryset)
        return Response(serializer.data)
