
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from main.models import Profile
from main.serializers import ProfileSerializer, PointsSerializer, ProfileUpdateSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileSerializer
        elif self.action == 'create':
            return ProfileSerializer
        elif self.action == 'update':
            return ProfileUpdateSerializer
        elif self.action == 'destroy':
            return ProfileSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def profile_detail(self, request, pk):
        queryset = Profile.objects.filter(id=pk)
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['PUT'], detail=False, permission_classes=(AllowAny,))
    def nullify(self, request):
        queryset = Profile.objects.update(points=0)
        serializer = PointsSerializer(queryset)
        return Response(serializer.data)
