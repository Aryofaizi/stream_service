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
        fields = ["id", "title", "description", "release_date",
                  "genre", "category", "rate","price"]
        
    def create(self, validated_data):
        genre_list = validated_data.pop("genre")
        
        content = models.Content.objects.create(**validated_data)
        
        for genre_data in genre_list:
            genre = models.Genre.objects.get(title=genre_data.get("title"))
            content.genre.add(genre)
            
        content.save()
        return content
    
    def update(self, instance, validated_data):
        genre_list = validated_data.pop("genre", None)
        
        
        # update non-many-to-many fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
          # Save the instance to ensure it's updated before modifying many-to-many field
        instance.save()
        
        
        if genre_list is not None:
            # Clear the existing genres
            instance.genre.clear() 
            
        # Retrieve and add new Genre instances
        for genre_data in genre_list:
            genre = models.Genre.objects.get(title=genre_data.get("title"))
            instance.genre.add(genre)
        # Return the updated instance
        return instance
         
        
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