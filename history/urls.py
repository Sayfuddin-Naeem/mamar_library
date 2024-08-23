from django.urls import path
from .views import BorrowNowView, ReturnView

urlpatterns = [
    path('borrow/<int:book_id>', BorrowNowView.as_view(), name='borrow_now'),
    path('return/<int:borrow_id>', ReturnView.as_view(), name='return_now'),
]
