from itertools import product
from unicodedata import category
from rest_framework import viewsets
from rest_framework.response import Response
from ourshop.models import Category, Product
from .serializer import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = Category.objects.all()
        return category


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product