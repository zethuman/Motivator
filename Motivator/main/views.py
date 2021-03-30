from django.shortcuts import render
from rest_framework import viewsets, renderers, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from main.models import Points
from main.serializers import PointsSerializer


class PointsViewSet(viewsets.ModelViewSet):
    queryset = Points.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return PointsSerializer
        elif self.action == 'create':
            return PointsSerializer
        elif self.action == 'update':
            return PointsSerializer
        elif self.action == 'destroy':
            return PointsSerializer
