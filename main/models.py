from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileModel(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    years_old = models.DateField()
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.name.username


class CategoryModel(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class ProductModel(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    category = models.ManyToManyField(CategoryModel, related_name='products')

    def __str__(self):
        return self.name
