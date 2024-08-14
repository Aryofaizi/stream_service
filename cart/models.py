from django.db import models
from uuid import uuid4
from content.models import Content

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="cart_items")
    
    class Meta:
        unique_together = [["cart", "content"]]
