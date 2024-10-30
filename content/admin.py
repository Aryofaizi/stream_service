from django.contrib import admin
from .models import Content, Genre, Comment, Video, Subtitle

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    model = Content
    list_display = [field.name for field in model._meta.fields]




@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = [field.name for field in model._meta.fields]
    
    
@admin.register(Comment)
class CommentAmin(admin.ModelAdmin):
    model = Comment
    list_display = [field.name for field in model._meta.fields]
    
    

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    model = Video
    list_display = [field.name for field in model._meta.fields]
    

@admin.register(Subtitle)
class SubtitleAdmin(admin.ModelAdmin):
    model = Subtitle
    list_display = [field.name for field in model._meta.fields]