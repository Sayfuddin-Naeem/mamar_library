from django.contrib import admin
from .models import Category

# Register your models here.
# admin.site.register(models.Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']
    
    def name(self, obj):
        return obj.name
    name.short_description = 'Category Name'
    
    def slug(self, obj):
        return obj.slug
    slug.short_description = 'Slug'