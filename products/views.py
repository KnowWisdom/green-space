from math import prod
from pstats import Stats
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .serializer import ProductSerializer

# APIView 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Product 목록 보기
class ProductList(APIView):
    # list 전송
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    
# Product 세부사항 보기
class ProductDetail(APIView):
    def get_object(self, pk):
        try :
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

