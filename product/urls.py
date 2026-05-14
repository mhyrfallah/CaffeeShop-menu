from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.product_menu, name='product_list')
]