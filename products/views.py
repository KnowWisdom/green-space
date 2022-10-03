from math import prod
from pstats import Stats
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .serializer import ProductSerializer

# APIView 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from django.http import Http404

# Product 목록 보기
class ProductList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # list 전송
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
# Product 세부사항 보기
class ProductDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

