from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from books.models import Book
from history.models import BorrowHistory
from reviews.forms import ReviewForm

# Create your views here.

class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'book_id'
    template_name = 'books/book_details.html'
    
    def post(self, request, *args, **kwargs):
        book = self.get_object()
        review_form = ReviewForm(data = self.request.POST)
        if review_form.is_valid():
            review_form.instance.book = book
            review_form.instance.name = f"{request.user.first_name} {request.user.last_name}"
            review_form.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['reviews'] = book.review.all()

        if self.request.user.is_authenticated:
            context['borrow'] = BorrowHistory.objects.filter(
                                        book=book,
                                        user=self.request.user
                                    ).order_by(
                                        '-transaction__timestamp'
                                    ).first()
            context['review_form'] = ReviewForm()

        return context