from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductsView(APIView):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        products = category.products.filter(status=Product.PRODUCT_AVAILABLE)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        