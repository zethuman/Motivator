from django.urls import path

from volunteering_module.views import VolunteerListAPIView, VolunteerDetailAPIView, CertificateViewSet

urlpatterns = [
    path('volunteer/', VolunteerListAPIView.as_view()),
    path('volunteer/<int:pk>/', VolunteerDetailAPIView.as_view()),
    path('volunteer/<int:pk>/certificates/', CertificateViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('volunteer/<int:pk>/certificates/<int:ek>/', CertificateViewSet.as_view({'get': 'certificate_detail_get',
                                                                                  'put': 'certificate_detail_update',
                                                                                  'delete': 'certificate_detail_delete'})),
]

