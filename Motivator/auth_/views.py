import logging

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auth_.models import MainUser
from auth_.serializers import UserSerializer

logger = logging.getLogger(__name__)


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()
    permission_classes = (AllowAny, )

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializer

    @action(methods=['POST'], detail=False, permission_classes = AllowAny )
    def post_user(self, request):
        user = request.data
        queryset = MainUser.objects.create_user(email=user['email'], password=user['password'], first_name=user['first_name'], last_name=user['last_name'], role=user['role'])
        queryset.save()
        logger.debug(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        logger.info(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        logger.warning(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        logger.error(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        logger.critical(f'User created ID: {queryset.id}' f' with email {queryset.email}')
        return Response(user, status=status.HTTP_201_CREATED)
