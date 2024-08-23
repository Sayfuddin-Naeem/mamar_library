from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from books.models import Book
from category.models import Category
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.contrib import messages

class HomeView(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['slCat'] = None
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            context['slCat'] = get_object_or_404(Category, slug=category_slug)
        return context