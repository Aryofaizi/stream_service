from django.contrib import admin
from .models import Order, OrderItem



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = [field.name for field in model._meta.fields]
    
    
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = [field.name for field in model._meta.fields]
