from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Prefetch


class OrderViewSet(ModelViewSet):
    http_method_names = ["get", "post", "delete", "options", "head"]
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user).prefetch_related(Prefetch(
                "items", queryset=OrderItem.objects.prefetch_related("content__genre")
            ))
    
    def get_serializer_context(self):
        context = {"user" : self.request.user}
        return context



class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer
    
    
    def get_queryset(self):
        order_id = self.kwargs["order_pk"]
        return OrderItem.objects.filter(order=order_id).prefetch_related("content__genre")