from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'date_added']

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
