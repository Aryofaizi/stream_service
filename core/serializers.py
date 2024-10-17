from djoser.serializers import UserSerializer as DjoserUserSerializer
from rest_framework import serializers


class CustomUserSerializer(DjoserUserSerializer):
    phone_number = serializers.CharField(read_only=True)
    
    class Meta(DjoserUserSerializer.Meta):
        fields = DjoserUserSerializer.Meta.fields + ('phone_number',)
        
    