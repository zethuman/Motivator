import logging

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from auth_.models import MainUser
from auth_.serializers import UserSerializer, PasswordSerializer
from Motivator.settings import LOGGING

logger = logging.getLogger(__name__)


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializer

    @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
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


# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     # Allow only authenticated users to access this url
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         # serializer to handle turning our `User` object into something that
#         # can be JSONified and sent to the client.
#         serializer = self.serializer_class(request.user)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         serializer_data = request.data.get('user', {})
#
#         serializer = UserSerializer(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)

# def upload(request):
#     if request.user.is_authenticated:
#         # Is it better to use @login_required ?
#         username = request.user.username
#     else:
#         username = ''
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             doc = form.save()
#             return render(request, 'app/upload.html', {
#                "form": DocumentForm(),
#                "uploaded_file_url": doc.myfile.url,
#                "username": username,
#             })
#     else:
#         form = DocumentForm()
#     return render(request, 'app/upload.html', {"form": form})
