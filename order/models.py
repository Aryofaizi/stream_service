from django.db import models
from config.settings import AUTH_USER_MODEL
from content.models import Content


class Order(models.Model):
    ORDER_STATUS_PAID = 'p'
    ORDER_STATUS_UNPAID = 'u'
    ORDER_STATUS_CANCELED = 'c'
    ORDER_STATUS = [
        (ORDER_STATUS_PAID,'Paid'),
        (ORDER_STATUS_UNPAID,'Unpaid'),
        (ORDER_STATUS_CANCELED,'Canceled'),
    ]
    
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='orders')
    datetime_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default=ORDER_STATUS_UNPAID)
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    content = models.ForeignKey(Content, on_delete=models.PROTECT, related_name='order_items')
    unit_price = models.PositiveIntegerField()

    class Meta:
        unique_together = [['order', 'content']]
    
