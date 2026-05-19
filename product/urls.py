from django.urls import path, include

from . import views

urlpatterns = [
    path('api/menu/', views.menu_list, name='category_list'),
    # path('', views.product_menu, name='product_list')
]