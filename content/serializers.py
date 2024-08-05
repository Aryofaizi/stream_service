from rest_framework import serializers
from . import models


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ["title", "description", "release_date",
                  "genre", "category", "rate","price"]
        
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ["user", "content", "text", "status",
                  "rate", "datetime_created", "datetime_modified"]
        read_only_fields = ["status", "user", "content"]