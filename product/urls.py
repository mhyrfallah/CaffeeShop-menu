from django.urls import path
from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('products/', CategoryListView.as_view(), name='category-list'),
    path('products/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
]