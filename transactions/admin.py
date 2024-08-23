from django.contrib import admin
from .models import Transaction

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type']
    
    def account(self, obj):
        return obj.account
    account.short_description = 'Account'
    
    def amount(self, obj):
        return obj.amount
    amount.short_description = 'Transaction Amount'
    
    def balance_after_transaction(self, obj):
        return obj.balance_after_transaction
    balance_after_transaction.short_description = 'Balance After Transaction'
    
    def transaction_type(self, obj):
        return obj.get_transaction_type_display()
    transaction_type.short_description = 'Transaction Type'
