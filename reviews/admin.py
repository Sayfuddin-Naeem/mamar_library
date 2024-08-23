from django.contrib import admin
from .models import Review

# Register your models here.
# admin.site.register(models.Category)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'name', 'body', 'created_on']
    
    def book(self, obj):
        return obj.book.title
    book.short_description = 'Book Name'
    
    def name(self, obj):
        return obj.name
    name.short_description = 'Review By'
    
    def body(self, obj):
        return obj.body
    body.short_description = 'Review'
    
    def created_on(self, obj):
        return obj.created_on
    created_on.short_description = 'Date-Time'