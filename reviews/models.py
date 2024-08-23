from django.db import models
from books.models import Book

# Create your models here.

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add='True')