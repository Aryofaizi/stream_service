from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["content", "unit_price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ["id", "status", "items"]
        read_only_fields = ["id", "status", "items"]
        
    def create(self, validated_data):
        user = self.context.get("user")
        order = Order.objects.create(user_id=user.id)
        order.save()
        return order