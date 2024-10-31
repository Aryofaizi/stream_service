from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Notification

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
    

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = [field.name for field in model._meta.fields]