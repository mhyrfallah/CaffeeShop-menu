from django.shortcuts import render
from django.views import generic
from .models import Product, Categories

class ProductMenu(generic.DetailView):
    model = Product
    context_object_name = Product
    template_name = '#'