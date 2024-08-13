from rest_framework import serializers
from . import models

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ["id"]
        read_only_fields = ["id"]