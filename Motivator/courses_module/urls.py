from django.urls import path

from courses_module.views import CourseViewSet,list_contents_by_course,content_by_course,CertificateViewSet

urlpatterns = [
    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'course_detail',
                                                     'put': 'update',
                                                     'delete': 'destroy'})),
    path('courses/<int:pk>/contents/', list_contents_by_course),
    path('courses/<int:pk>/contents/<int:ek>/', content_by_course),

    path('courses/<int:pk>/certificates/', CertificateViewSet.as_view({'get': 'list','post': 'create'})),
    path('courses/<int:pk>/certificates/<int:ek>/', CertificateViewSet.as_view({'get': 'certificate_detail_get',
                                                                                 'put': 'certificate_detail_update',
                                                                                 'delete': 'certificate_detail_delete'})),
]

