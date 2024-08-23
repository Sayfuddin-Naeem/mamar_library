from django.contrib import admin
from .models import BorrowHistory

# Register your models here.
# admin.site.register(models.Category)
@admin.register(BorrowHistory)
class BorrowHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'price', 'date', 'type']
    
    def user(self, obj):
        return obj.user.username
    user.short_description = 'User'
    
    def book(self, obj):
        return obj.book.title
    book.short_description = 'Book Name'
    
    def price(self, obj):
        return obj.book.price
    price.short_description = 'Book Price'
    
    def date(self, obj):
        return obj.transaction.timestamp
    date.short_description = 'Date-Time'
    
    def type(self, obj):
        return obj.transaction.get_transaction_type_display()
    type.short_description = 'Action'