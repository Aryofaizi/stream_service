from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer
from .models import Cart, CartItem
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from django.db.models import Prefetch

class CartViewSet(CreateModelMixin,
                  RetrieveModelMixin, GenericViewSet,
                  DestroyModelMixin):
    serializer_class = CartSerializer
    queryset = Cart.objects.all().prefetch_related(Prefetch(
        "items", CartItem.objects.prefetch_related("content__genre")
        ))
    

class CartItemViewSet(ModelViewSet):
    http_method_names = ["get","post","delete"]
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    
    def get_queryset(self):
        cart_id = self.kwargs["cart_pk"]
        return CartItem.objects.filter(cart=cart_id)
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        context = {"cart_pk" : self.kwargs["cart_pk"]}
        return context