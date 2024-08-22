from rest_framework import serializers
from . import models
from content.serializers import ContentSerializer
from django.shortcuts import get_object_or_404


class CartItemSerializer(serializers.ModelSerializer):
    content = ContentSerializer(read_only=True)
    class Meta:
        model = models.CartItem
        fields = ["content"]
        read_only_fields = ["content"]
        
class AddCartItemSerializer(serializers.ModelSerializer):
    content = serializers.PrimaryKeyRelatedField(queryset=models.Content.objects.all())
    class Meta:
        model = models.CartItem
        fields = ["content"]
        
          
    def create(self, validated_data):
        cart = get_object_or_404(models.Cart, pk=self.context.get("cart_pk"))
        content = validated_data["content"]
        cart_item = models.CartItem()
        cart_item.cart = cart
        cart_item.content = content
        cart_item.save()
        return cart_item

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = models.Cart
        fields = ["id", "items"]
        read_only_fields = ["id", "items"]
        
        
