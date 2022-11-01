from distutils.log import error
from email import header
from gc import get_objects
from os import stat
import re
from signal import raise_signal
from urllib import request
from django.shortcuts import render
from .serializers import *
from .models import Item, Buy
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView

# =========================================================== #
# Item 목록 보기 / 수정 / 삭제 
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    


# =========================================================== #
# BUY

class BuyList(APIView):
    
    # 해당 사용자가 구매한 아이템 리스트
    def get(self, request):
        buys = Buy.objects.filter(user=request.user)
        serializers = BuyDetailSerializer(buys, many=True)
        return Response(serializers.data)

    # 아이템 구매
    def post(self, request):
        request.data['user'] = request.user.user_id

        if Buy.objects.filter(user=request.user, item=request.data['item']).exists :
            return Response({
                "message" : "이미 구매했습니다."
            }, status=status.HTTP_400_BAD_REQUEST)
        else :
            serializer = BuySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                item = Buy.objects.get(id=request.data['item'])
                data = {
                    "nickname" : request.user.user_id,
                    "item" : item.item.name,
                }
                return Response(data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # 보유 중인 아이템 되팔기
    def delete(self, request, format=None):
        item = Item.objects.get(name=request.data['name'])
        # item=Item.objects.get(id=pk)    

        try:
            buy = Buy.objects.get(user=request.user.user_id, item=item)
        except :
            return Response({
                "message" : "해당 아이템을 소유하고 있지 않습니다."
            }, status=status.HTTP_400_BAD_REQUEST)
        if request.user.point < 10 :
            return Response({
                "message": "포인트가 적습니다."
            }, status=status.HTTP_400_BAD_REQUEST)
        else :
            buy.delete()
            user = CustomUser.objects.filter(user_id = request.user.user_id)
            print(item.point)
            user.update(point= user[0].point + (item.point)/2)
            return Response({
                "message" : "포인트를 " + str(item.point/2) +" 만큼 획득하고 삭제 성공"
            },status=status.HTTP_204_NO_CONTENT)


