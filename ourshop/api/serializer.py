from dataclasses import fields
from rest_framework import serializers
from ourshop.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'categories', 'approved_by', 'user', 'approved', 'display_on_main_page']
        depth =1           # for nested data (field - categories)