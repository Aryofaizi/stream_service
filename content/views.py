from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models
from .permissions import IsAdminOrReadOnly


class ContentViewSet(ModelViewSet):
    serializer_class = serializers.ContentSerializer
    queryset = models.Content.objects.all()
    permission_classes = [IsAdminOrReadOnly]
