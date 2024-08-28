from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(ModelViewSet):
    http_method_names = ["get", "post", "delete", "options", "head"]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_context(self):
        context = {"user" : self.request.user}
        return context
