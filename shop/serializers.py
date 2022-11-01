from django.contrib.auth import get_user_model
from .models import Item, Buy
from rest_framework import serializers

CustomUser = get_user_model()

# Item
class ItemSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True)

    class Meta :
        model = Item
        fields = ['name', 'image', 'point', 'category']

# Buy
class BuyDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.nickname")
    item = ItemSerializer()
    
    class Meta : 
        model = Buy
        fields = '__all__'

class BuySerializer(serializers.ModelSerializer):
    class Meta :
        model = Buy
        fields = ['user', 'item']
