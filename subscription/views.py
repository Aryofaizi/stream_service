from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import SubscriptionPlanSerializer
from . import models



class SubscriptionPlanViewSet(ModelViewSet):
    http_method_names = ["get", "post"]
    serializer_class = SubscriptionPlanSerializer
    queryset = models.SubscriptionPlan.objects.all()
