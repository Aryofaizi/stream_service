from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("contents",views.ContentViewSet,basename="content")


urlpatterns = router.urls



