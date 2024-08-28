from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "status"]
        read_only_fields = ["id", "status", ]
        
    def create(self, validated_data):
        user = self.context.get("user")
        order = Order.objects.create(user_id=user.id)
        order.save()
        return order