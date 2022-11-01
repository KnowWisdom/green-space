from django.contrib.auth import get_user_model
from .models import Post
from rest_framework import serializers

CustomUser = get_user_model()

class PostSerializer(serializers.ModelSerializer):

    class Meta :
        model = Post
        fields = ['id', 'image', 'text', 'created_at', 'updated_at']

class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.nickname')

    class Meta :
        model = Post
        fields = ['user', 'image', 'text']