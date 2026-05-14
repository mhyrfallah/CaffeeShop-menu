from django.contrib import admin
from .models import Product, Categories

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'date_added']

@admin.register(Categories)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
