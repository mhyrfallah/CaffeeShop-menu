from django.urls import path
from .views import CategoryListView, CategoryProductsView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/products/', CategoryProductsView.as_view(), name='category-products'),
]