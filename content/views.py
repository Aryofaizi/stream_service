from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers
from . import models

class ContentViewSet(ModelViewSet):
    serializer_class = serializers.ContentSerializer
    queryset = models.Content.objects.all()
    
