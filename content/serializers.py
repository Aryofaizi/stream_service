from rest_framework import serializers
from . import models
from core.models import CustomUser

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ["title"]

class ContentSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    class Meta:
        model = models.Content
        fields = ["title", "description", "release_date",
                  "genre", "category", "rate","price"]
        
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CustomUser
        fields = ["username"]
        read_only_fields = ["username"]
        
class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = models.Comment
        fields = ["user", "content", "text", "status",
                  "rate", "datetime_created", "datetime_modified"]
        read_only_fields = ["status", "user", "content"]