from django.shortcuts import render
from .models import Notification
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def mark_all_notifications_as_read(request):
    """makes notification.is_read = True."""
    queryset = request.user.notifications.filter(is_read=False)
    count = queryset.count()
    if count > 0 :
        queryset.update(is_read=True)
        return Response({"status": "success", "message": f"{count} notifications marked as read."})
    else:
        return Response({"status": "info", "message": "No unread notifications to mark as read."})
    
