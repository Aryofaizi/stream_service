from django.db.models.signals import post_save
from .models import Notification
from django.dispatch import receiver
from content.models import Comment

@receiver(post_save, sender=Comment)
def create_approval_notificaiton(sender, instance, **kwargs):
    if instance.status == "a":
        Notification.objects.create(
            user = instance.user,
            message = "you comment has been approved!"
        )