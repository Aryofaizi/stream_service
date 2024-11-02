from django.shortcuts import render, get_object_or_404
from .models import Notification
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from content.models import Content
from rest_framework.views import APIView
from urllib.parse import quote

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
    



# social networking 
class GenerateShareableLink(APIView):
    permission_classes = [IsAuthenticated]
    """generate shareable links to use in social medias."""
    def get(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        share_url = request.build_absolute_uri(content.get_absolute_url)
        encoded_title = quote(content.title)
        
        share_links = {
            'twitter': f'https://twitter.com/intent/tweet?text={encoded_title}&url={quote(share_url)}',
            'facebook': f'https://www.facebook.com/sharer/sharer.php?u={quote(share_url)}',
            'email': f'mailto:?subject={encoded_title}&body={quote("Check this out:")} {quote(share_url)}'
        }
        return Response({"share_links":share_links})