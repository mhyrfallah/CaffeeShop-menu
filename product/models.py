from django.db import models

# Custom User


# Product model

class Categories(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Product(models.Model):

    # category
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name