from dataclasses import field
from .models import Item, Buy
from rest_framework import serializers

# Item
class ItemSerializer(serializers.ModelSerializer):
    class Meta :
        model = Item
        fields = '__all__'


# Buy
class BuySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta :
        model = Buy
        fields = '__all__'
