from collections import UserList
from os import stat
from urllib import response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import CustomUser
from .serializers import *
from django.db.models import Q
from .models import CustomUser, Follow

class CustomUserView(APIView):
    permission_classes = [ AllowAny ]

    def post(self, request):
        reg_serializer = CustomUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save() # Query Type
            
            return Response(
                {
                    "user": CustomUserSerializer(new_user).data, # JSON Type
                    "message": "회원가입이 완료되었습니다!"
                },
                status = status.HTTP_201_CREATED,
            )
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserListView(APIView):
    permission_classes = [ IsAuthenticated ]
    
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.filter(~Q(user_id=request.user.user_id) & ~Q(open = False))
        serializers = UserListSerializer(users, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)        
    


class SignInUserView(APIView):
    permission_classes = [ AllowAny ]

    def post(self, request):
        nickname = request.data.get("nickname")
        password = request.data.get("password")
        if not nickname or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(
            nickname = nickname,
            password = password,
        )
        if user:
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)

            res = Response(
                {
                    "refresh": str(token),
                    "access": str(token.access_token),
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class SignOutUserView(APIView):
    permission_classes = [ IsAuthenticated ]

    def post(self, request, *args):
        user = RefreshTokenSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        reset = ''
        res = Response(
            {
                "message": "logout success" 
            }, status=status.HTTP_204_NO_CONTENT
        )
        res.set_cookie('access', reset)
        res.set_cookie('refresh', reset)

        return Response(
                {
                    "message": "logout success" 
                }, status=status.HTTP_204_NO_CONTENT)


class DeleteUserView(APIView):
    def delete(self, request):
        User = CustomUser.objects.get(user_id=request.user.user_id)
        User.delete()
        return Response(status=status.HTTP_200_OK)


class ProfileView(APIView):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(user_id=request.user.user_id)
            
        return Response(
            {
                "user_id": user.user_id,
                "username": user.username,
                "point" : user.point,
                "open" : user.open,
            }
        )

    def patch(self, request):
        user = CustomUser.objects.get(user_id=request.user.user_id)
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class FollowingView(APIView):
    def post(self, request, *args):
        follow_nickname = request.data["nickname"]

        if not follow_nickname :
            return Response({
                "messmage" : "key error"
            }, status = status.HTTP_400_BAD_REQUEST)

        from_user = request.user
        to_user = CustomUser.objects.get(nickname=follow_nickname)
        follow = Follow.objects.filter(from_user=from_user, to_user=to_user)

        if follow :
            follow[0].delete()
            message = 'unfollowing'
        else :
            Follow.objects.create(
                from_user = from_user,
                to_user = to_user,
            )
            message = 'following'

        return Response({
            "message" : message
        }, status=status.HTTP_200_OK)

class FollowingListView(APIView):
    def get(self, request):
        to_user = Follow.objects.filter(from_user = request.user)

        if to_user.exists():
            serializers = ToUserSerializer(to_user, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({
                "message" : "해당 사용자가 팔로잉하고있는 사용자가 없음"
            })




class FollowedListView(APIView):
    def get(self, request):
        from_user = Follow.objects.filter(to_user = request.user)
        if from_user.exists():
            serializers = FromUserSerializer(from_user, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({
                "message" : "해당 사용자를 팔로우하는 사용자가 없음"
            })
