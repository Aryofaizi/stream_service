from rest_framework import serializers
from .models import Order, OrderItem
from content.serializers import ContentSerializer
from content.models import Content



class AddOrderItemSerilizer(serializers.ModelSerializer):
    content = serializers.PrimaryKeyRelatedField(queryset=Content.objects.all())
    class Meta: 
        model = OrderItem
        fields = ["content", "unit_price"]
        
    def create(self, validated_data):
        order = Order.objects.get(pk=self.context.get("order_id"))
        order_item = OrderItem.objects.create(
            order = order, **validated_data
        )
        order_item.save()
        return order_item

class OrderItemSerializer(serializers.ModelSerializer):
    content = ContentSerializer()
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