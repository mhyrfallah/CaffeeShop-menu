from rest_framework import serializers
from .models import Categories, Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['id', 'name', 'products']