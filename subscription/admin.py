from django.contrib import admin
from .models import SubscriptionPlan, UserSubscription

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    model = SubscriptionPlan
    list_display = [field.name for field in model._meta.fields]


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    model = UserSubscription
    list_display = [field.name for field in model._meta.fields]