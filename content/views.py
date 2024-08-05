from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models
from .permissions import IsAdminOrReadOnly, IsOwner
from rest_framework import permissions


class ContentViewSet(ModelViewSet):
    serializer_class = serializers.ContentSerializer
    queryset = models.Content.objects.all()
    permission_classes = [IsAdminOrReadOnly]



class CommentViewSet(ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsOwner]
    def get_queryset(self):
        return models.Comment.objects.filter(content_id =self.kwargs.get("content_pk"))
    