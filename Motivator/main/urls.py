from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from main.views import ProfileViewSet

urlpatterns = [
    path('profile/', ProfileViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'nullify'})),
    path('profile/<int:pk>/', ProfileViewSet.as_view({'get': 'profile_detail',
                                                      'put': 'update',
                                                      'delete': 'destroy'})),

]
