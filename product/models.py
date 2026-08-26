from email.policy import default
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Custom User

class CustomUserModel(AbstractBaseUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Product(models.Model):
    PRODUCT_WAITING = 'w'
    PRODUCT_UNAVAILABLE = 'ua'
    PRODUCT_AVAILABLE = 'a'

    PRODUCT_STATUS = [
        (PRODUCT_WAITING, 'waiting'),
        (PRODUCT_UNAVAILABLE, 'unavailable'),
        (PRODUCT_AVAILABLE, 'available'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item_set')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=2, default=PRODUCT_WAITING, choices=PRODUCT_STATUS)
    slug = models.SlugField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
