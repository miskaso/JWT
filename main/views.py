from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import ProductModel, CategoryModel
from .serializers import UserSerializer, ProductSerializer, CategorySerializer


# Create your views here.


class ProfileView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [AllowAny]


class ProductView(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        operation_description="Получить все продукты",
        responses={200: ProductSerializer(many=True), 404: 'Продукция не найдена'}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Получить один объект',
        responses={200: ProductSerializer(many=False), 404: 'Продукт не найден'}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Добавить объект',
        responses={201: ProductSerializer, 404: 'Продукт отсутствует'},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Название продукта'),
                'desc': openapi.Schema(type=openapi.TYPE_STRING, description='Описаение продукта'),
                'category': openapi.Schema(type=openapi.TYPE_STRING, description='Категория продукта')
            },
            required=['name', 'desc', 'category'],
            example={
                'name': 'Product',
                'desc': 'BLa Bla bla bla',
                'category': 'Select category product'
            }
        )
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    permission_classes = [AllowAny]


class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
