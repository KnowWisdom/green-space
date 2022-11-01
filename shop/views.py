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
from django.db.models import Q

# =========================================================== #
# Item 목록 보기 / 수정 / 삭제 
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(category='item')
    serializer_class = ItemSerializer
    
class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.filter(category='badge')
    serializer_class = ItemSerializer


# =========================================================== #
# BUY

class SpaceView(APIView):
    def get(self, request):
        space = Buy.objects.filter(pick = True, user = request.user)
        serializer = BuyDetailSerializer(space, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        user = CustomUser.objects.get(nickname = request.data["nickname"])
        space = Buy.objects.filter(pick = True, user = user)
        serializer = BuyDetailSerializer(space, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class BuyList(APIView):
    
    # 해당 사용자가 구매한 아이템 리스트
    def get(self, request):
        buys = Buy.objects.filter(user=request.user)
        serializers = BuyDetailSerializer(buys, many=True)
        return Response(serializers.data)

    # 아이템 구매
    def post(self, request):
        request.data['user'] = request.user.user_id
        item = Item.objects.get(name=request.data['item'])

        if Buy.objects.filter(user=request.user, item=item).exists() :
            return Response({
                "message" : "이미 구매했습니다."
            }, status=status.HTTP_400_BAD_REQUEST)
        else :
            request.data['category'] = item.category
            print(request.data)

            serializer = BuySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                buys = Buy.objects.filter(user=request.user)
                detail_serializer = BuyDetailSerializer(buys, many=True)
                return Response(detail_serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # 보유 중인 아이템 되팔기
    def delete(self, request, format=None):
        item = Item.objects.get(name=request.data['item'])
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

    def patch(self, request):
        item = Item.objects.get(name= request.data["item"])
        buy = Buy.objects.get(item=item)

        category = buy.category

        # 해당 카테고리에 다른 아이템이 선택되었는지 확인
        # 다른 아이템의 pick을 false로 바꾸고 선택한 아이템을 true로
        picked = Buy.objects.get(category=category, pick=True)
        print(picked.item.name)
        if not picked:
            buy.category = True
            buy.save()
        else:
            picked.pick = False
            buy.pick = True
            picked.save()
            buy.save()
        # 해당 카테고리에 선택된 다른 아이템이 없다면
        # 그냥 해당 buy의 pick을 true로

        buys = Buy.objects.filter(user=request.user)
        serializers = BuyDetailSerializer(buys, many=True)
        return Response(serializers.data)


