from django.contrib import admin
from .models import UserAccount, UserAddress

# Register your models here.
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date', 'gender', 'balance']
    
    def user(self, obj):
        return obj.user.username
    user.short_description = 'User'
    
    def birth_date(self, obj):
        return obj.birth_date
    birth_date.short_description = 'Birth Date'
    
    def gender(self, obj):
        return obj.get_gender_display()
    gender.short_description = 'Gender'
    
    def balance(self, obj):
        return obj.balance()
    balance.short_description = 'Account Balance'
    
@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'city', 'postal_code', 'country']
    
    def user(self, obj):
        return obj.user.username
    user.short_description = 'User'
    
    def street_address(self, obj):
        return obj.street_address
    street_address.short_description = 'Street Address'
    
    def city(self, obj):
        return obj.city
    city.short_description = 'City'
    
    def postal_code(self, obj):
        return obj.postal_code
    postal_code.short_description = 'Postal Code'
    
    def country(self, obj):
        return obj.country
    country.short_description = 'Country'