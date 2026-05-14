from django.shortcuts import render
from django.views import generic
from .models import Product, Categories

def product_menu(request):
    model = Product
    context = {'product': Product.objects.all()}

    return render(request, 'product.html', context)
