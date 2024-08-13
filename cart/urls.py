from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("", views.CartViewSet, "cart")


urlpatterns = router.urls
