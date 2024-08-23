from django.urls import path
from books.views import BookDetailView

urlpatterns = [
    path('details/<int:book_id>', BookDetailView.as_view(), name='book_detail'),
]
