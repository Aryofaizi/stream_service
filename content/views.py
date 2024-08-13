from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models
from .permissions import IsAdminOrReadOnly, IsOwner
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .paginations import ContentPagination

class ContentViewSet(ModelViewSet):
    serializer_class = serializers.ContentSerializer
    queryset = models.Content.objects.all().prefetch_related("genre")
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["title", "genre", "release_date", "category", "rate"]
    # optional ordering fields
    ordering_fields = ["rate"]
    #default value of ordering 
    ordering = ["-datetime_created"]
    search_fields = ['title']
    pagination_class = ContentPagination



class CommentViewSet(ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsOwner]
    
    
    def get_queryset(self):
        return models.Comment.objects.filter(
            content_id =self.kwargs.get("content_pk"), status=models.Comment.STATUS_APPROVED
            ).select_related("user")
    
    def get_serializer_context(self):
        context = {"user_id": self.request.user.id,
                   "content_pk": self.kwargs.get("content_pk")}
        return context