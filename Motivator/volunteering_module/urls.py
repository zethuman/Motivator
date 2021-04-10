from django.urls import path

from volunteering_module.views import VolunteerViewSet

urlpatterns = [
    path('volunteers/', VolunteerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('volunteers/<int:pk>/', VolunteerViewSet.as_view({'get': 'course_detail',
                                                     'put': 'update',
                                                     'delete': 'destroy'})),
]

