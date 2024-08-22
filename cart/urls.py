from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register("", views.CartViewSet, "cart")

cart_item_router = NestedDefaultRouter(router, "", lookup="cart")
cart_item_router.register("items", views.CartItemViewSet, "cart_item")

urlpatterns = router.urls + cart_item_router.urls
