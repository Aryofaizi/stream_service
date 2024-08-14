from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CartSerializer
from .models import Cart, CartItem
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from django.db.models import Prefetch

class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all().prefetch_related(Prefetch(
        "items", CartItem.objects.select_related("content")
        ))
    
