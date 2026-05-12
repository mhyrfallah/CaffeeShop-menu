from django.db import models

# Product model

class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    