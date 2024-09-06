from django.contrib import admin
from .models import ProfileModel, CategoryModel, ProductModel

# Register your models here.

admin.site.register(ProductModel)
admin.site.register(ProfileModel)
admin.site.register(CategoryModel)
