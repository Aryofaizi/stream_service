from rest_framework import serializers
from . import models


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ["title", "description", "release_date",
                  "genre", "category", "rate","price"]