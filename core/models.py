from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11)
    
    

class Notification(models.Model):
    """a class represents notification in database."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
         return f"Notification for {self.user.username}: {self.message[:50]}"
    
    
