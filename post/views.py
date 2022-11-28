from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status, viewsets
from .serializers import *
from .models import *
from shop.models import Buy, Item
from rest_framework.response import Response

# Create your views here.

class PostListView(APIView):
    # 사용자 게시물 리스트
    def get(self, request):
        posts = Post.objects.filter(user=request.user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 게시물 등록
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)

        if serializer.is_valid():
            post = Post.objects.create(
                user = request.user,
                image = request.data['image'],
                text = request.data['text'],
            )
            user = CustomUser.objects.get(user_id = request.user.user_id)
            user.point = user.point + 10
            user.save()
            if Post.objects.filter(user=request.user).count() == 10 :
                print("게시물 10개 달성")
                item = Item.objects.get(name='b.2')
                have = Buy.objects.filter(item=item, user=request.user)
                if have.exists():
                    pass
                else:
                    badge = Buy.objects.create(
                    user = request.user,
                    category = 'badge',
                    item = item,
                    )
            if Post.objects.filter(user=request.user).count() == 5:
                print("게시물 5개 달성")
                item = Item.objects.get(name='b.1')
                have = Buy.objects.filter(item=item, user=request.user)
                if have.exists():
                    pass
                else:
                    badge = Buy.objects.create(
                        user = request.user,
                        category = 'badge',
                        item = item,
                    )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 게시물 삭제
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        user = CustomUser.objects.get(user_id = request.user.user_id)
        user.point = user.point - 10
        user.save()
        return self.destroy(request, *args, **kwargs)

