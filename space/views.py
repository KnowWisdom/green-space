from django.shortcuts import render
from .serializers import ItemSerializer, BuySerializer
from .models import Item, Buy
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated

# Item 목록 보기 / 수정 / 삭제 
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class BuyView(ListAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        user = request.user
        buy = Buy.objects.filter(user = user)
        serializer = BuySerializer(buy, many=True)
        return Response(serializer.data)


