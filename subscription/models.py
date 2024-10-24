from django.db import models
from django.conf import settings
from datetime import timedelta
from django.utils import timezone

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField()
    duration_in_days = models.PositiveIntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
class UserSubscription(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('canceled', 'Canceled'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.plan.name}"

    @property
    def expire_date(self):
        """Calculate expiration date based on start_date and plan duration."""
        # Use timezone.now() as a fallback if start_date is None
        start = self.start_date or timezone.now()
        return start + timedelta(days=self.plan.duration_in_days)

    def is_active(self):
        """Check if the subscription is active based on the current time and status."""
        return self.status == 'active' and timezone.now() < self.expire_date

    def save(self, *args, **kwargs):
        """Override save to auto-expire subscriptions based on current time."""
        if self.status == 'active' and timezone.now() > self.expire_date:
            self.status = 'expired'
        super(UserSubscription, self).save(*args, **kwargs)