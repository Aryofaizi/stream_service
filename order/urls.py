from rest_framework import routers
from .views import OrderViewSet

router = routers.DefaultRouter()
router.register("", OrderViewSet, "orders")


urlpatterns = router.urls
