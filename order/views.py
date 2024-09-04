from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer, AddOrderItemSerilizer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Prefetch
from rest_framework.exceptions import NotFound


class OrderViewSet(ModelViewSet):
    http_method_names = ["get", "post", "options", "head"]
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
    http_method_names = ["get", "post", "options", "head", "delete"]
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddOrderItemSerilizer
        return OrderItemSerializer
            
    def get_serializer_context(self):
        context = {"order_id":self.kwargs["order_pk"]}
        return context
    
    
    def get_queryset(self):
        order_id = self.kwargs["order_pk"]
        user = self.request.user

        # If the user is an admin, return all OrderItems for the specified order
        if user.is_staff:  # Check if the user is an admin
            try:
                order = Order.objects.get(pk=order_id)
            except Order.DoesNotExist: 
                raise NotFound("Order not found")    
            return OrderItem.objects.filter(order=order).prefetch_related("content__genre")
        # For regular users, ensure they only access their own orders
        try:
            order = Order.objects.get(pk=order_id, user=user)
        except Order.DoesNotExist:
            raise NotFound("Order not found or you do not have permission to access it.")

        return OrderItem.objects.filter(order=order).prefetch_related("content__genre")
    