from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CartSerializer
from .models import Cart
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    
