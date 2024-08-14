from rest_framework import serializers
from . import models
from content.serializers import ContentSerializer


class CartItemSerializer(serializers.ModelSerializer):
    content = ContentSerializer(read_only=True)
    class Meta:
        model = models.CartItem
        fields = ["content"]
        read_only_fields = ["content"]

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = models.Cart
        fields = ["id", "items"]
        read_only_fields = ["id", "items"]
        
        
