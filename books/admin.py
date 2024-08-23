from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(models.Category)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity', 'description', 'category']
    
    def title(self, obj):
        return obj.title
    title.short_description = 'Book Name'
    
    def price(self, obj):
        return obj.price
    price.short_description = 'Borrow Price'
    
    def quantity(self, obj):
        return obj.quantity
    quantity.short_description = 'Quantity'
    
    def description(self, obj):
        return obj.description
    description.short_description = 'Description'
    
    def category(self, obj):
        return obj.category.name
    category.short_description = 'Category'