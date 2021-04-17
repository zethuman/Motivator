from django.urls import path

from books_module.views import BookListAPIView, EssayListAPIView, BookDetailAPIView, essays_by_book

urlpatterns = [
    path('book_motivator/', BookListAPIView.as_view()),
    path('book_motivator/<int:pk>/', BookDetailAPIView.as_view()),
    path('book_motivator/<int:pk>/essays/', EssayListAPIView.as_view()),
    path('book_motivator/<int:pk>/essays/<int:ek>/', essays_by_book),
    # path('book_motivator/<int:pk>/essays/<int:ek>/', EssayDetailAPIView.as_view())
]

