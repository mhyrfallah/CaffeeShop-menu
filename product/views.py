from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import CategorySerializer
from .models import Category


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.prefetch_related('item_set')
        serializer = CategorySerializer(categories, many=True)

        data = {}
        for category in serializer.data:
            category['products'] = {p['id']: p for p in category['products']}
            data[category['slug']] = category

        return Response(data)


class CategoryDetailView(APIView):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        serializer = CategorySerializer(category)
        products = {p['id']: p for p in serializer.data['products']}
        return Response(products)