from django.db import transaction as db_transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import Book
from .models import BorrowHistory
from transactions.models import Transaction
from transactions.views import send_transaction_email
from django.views.generic import View
from transactions.constants import BORROW_BOOK, RETURN_BOOK

# Create your views here.
class BorrowNowView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        account = request.user.account
        
        if book.quantity > 0:
            if book.price <= account.balance:
                with db_transaction.atomic():
                    book.quantity -= 1
                    book.save()

                    account.balance -= book.price
                    account.save(update_fields=['balance'])

                    transaction = Transaction.objects.create(
                        account=account,
                        amount=book.price,
                        balance_after_transaction=account.balance,
                        transaction_type=BORROW_BOOK
                    )

                    BorrowHistory.objects.create(
                        user=request.user,
                        book=book,
                        transaction=transaction
                    )

                    messages.success(request, 'Book borrowed successfully!')
                    send_transaction_email(
                    user=self.request.user,
                    subject="Borrow Book",
                    common=book, 
                    template="history/borrow_book_email.html"
                )
            else:
                messages.error(request, 'Insufficient balance to borrow this book.')
        else:
            messages.error(request, 'Sorry, this book is out of stock.')

        return redirect('profile')
    
class ReturnView(LoginRequiredMixin, View):
    def post(self, request, borrow_id):
        borrow = get_object_or_404(BorrowHistory, id=borrow_id)
        account = request.user.account
        
        if borrow:
            book = borrow.book
            with db_transaction.atomic():
                book.quantity += 1
                book.save()

                account.balance += book.price
                account.save(update_fields=['balance'])

                Transaction.objects.create(
                    account=account,
                    amount=book.price,
                    balance_after_transaction=account.balance,
                    transaction_type=RETURN_BOOK
                )

                borrow.return_book = True
                borrow.save(update_fields=['return_book'])

                messages.success(request, 'Book returned successfully!')
                send_transaction_email(
                    user=self.request.user,
                    subject="Return Book",
                    common=book, 
                    template="history/return_book_email.html"
                )
        else:
            messages.error(request, 'Sorry, this book is not able to return for technical issue.')

        return redirect('profile')
