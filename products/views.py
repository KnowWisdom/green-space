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
from rest_framework import viewsets

# Product 목록 보기
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

