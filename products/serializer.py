from dataclasses import field
from .models import Product, Bookmark
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = '__all__'

class BookmarkSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta :
        model = Bookmark
        fields = ['id', 'product']