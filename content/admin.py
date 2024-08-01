from django.contrib import admin
from .models import Content, Genre

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    model = Content
    list_display = [field.name for field in model._meta.fields]




@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = [field.name for field in model._meta.fields]