from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class Category(models.Model):

    category_name = models.CharField(max_length=50)


class Product(models.Model):

    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    brand = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)