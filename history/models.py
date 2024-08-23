from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from books.models import Book
from transactions.models import Transaction

# Create your models here.

class BorrowHistory(models.Model):
    user = models.ForeignKey(User, related_name='user_history', verbose_name=_("User"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_history', verbose_name=_("Borrow Book"), on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, related_name='transaction_history', verbose_name=_("Transactions History"), on_delete=models.CASCADE)
    return_book = models.BooleanField(default=False)
    