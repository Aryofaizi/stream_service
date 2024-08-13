from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """represent Cart Model in AdminPanel to be editable."""
    model = Cart
    list_display = [field.name for field in model._meta.fields]
    
    

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """represent CartItem Model in AdminPanel to be editable."""
    model = CartItem
    list_display = [field.name for field in model._meta.fields]
    
