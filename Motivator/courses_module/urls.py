from django.urls import path

from books_module.views import BookListAPIView, EssayListAPIView, BookDetailAPIView, EssayDetailAPIView
from courses_module.views import CourseViewSet

urlpatterns = [
    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'course_detail',
                                                     'put': 'update',
                                                     'delete': 'destroy'})),
]

