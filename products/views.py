from math import prod
from pstats import Stats
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product,Bookmark
from .serializer import ProductSerializer, BookmarkSerializer

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

# 북마크 설정
class BookmarkView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)

        bookmark = Bookmark.objects.filter(product = product, user = request.user)

        if bookmark :
            bookmark[0].delete()
            message = "북마크 해제"
        else :
            Bookmark.objects.create(
                user = request.user,
                product = product,
            )
            message = "북마크 등록"
        return Response({
            "message" : message
        }, status=status.HTTP_200_OK)

class BookmarkListView(APIView):
    def get(self, request):
        bookmark = Bookmark.objects.filter(user = request.user)
        serializer = BookmarkSerializer(bookmark, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



