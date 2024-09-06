from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ProductModel, ProfileModel, CategoryModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['years_old', 'address', 'contact']


class UserSerializer(serializers.ModelSerializer):
    name = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'name']

    def create(self, validated_data):
        name_data = validated_data.pop('name')
        user = User.objects.create(**validated_data)
        ProfileModel.objects.create(name=user, **name_data)

        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['name', 'desc', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['category']