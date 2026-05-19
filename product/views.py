from django.shortcuts import render
from django.views import generic
from .models import Product, Categories
from rest_framework.decorators import api_view
from .serializers import CategorySerializer
from rest_framework.response import Response


@api_view(['GET'])
def category_list(request):
    categories = Categories.objects.prefetch_related('products').all()
    
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)


# @api_view(['GET'])
# def menu_list(request):
#     items = Categories.objects.all()
#     serializer = MenuItemSerializer(items, many=True)
#     return Response(serializer.data)


# def product_menu(request):
#     model = Product
#     context = {'product': Product.objects.all()}

#     return render(request, 'product.html', context)
