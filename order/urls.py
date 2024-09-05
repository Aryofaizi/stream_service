from rest_framework import routers
from .views import OrderViewSet, OrderItemViewSet
from rest_framework_nested.routers import NestedDefaultRouter


router = routers.DefaultRouter()
router.register("", OrderViewSet, "order")
order_item_router = NestedDefaultRouter(router, "", lookup="order")
order_item_router.register("items", OrderItemViewSet, basename="order-item")


urlpatterns = router.urls + order_item_router.urls
