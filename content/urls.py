from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from . import views

router = DefaultRouter()
router.register("contents", views.ContentViewSet, basename="content")


#nested 
content_router = NestedDefaultRouter(router, "contents", lookup="content")
content_router.register("comments", views.CommentViewSet, basename="content-comment")

urlpatterns = router.urls + content_router.urls



