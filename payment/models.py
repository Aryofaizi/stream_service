from django.db import models
from config.settings import AUTH_USER_MODEL
from subscription.models import SubscriptionPlan


class Payment(models.Model):
    """payment model class."""
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    is_paid = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    zarinpal_authority = models.CharField(max_length=255, blank=True)
    zarinpal_ref_id = models.CharField(max_length=150, blank=True)
    zarinpal_data = models.TextField(blank=True)
    has_been_sent  = models.BooleanField(default=False)
