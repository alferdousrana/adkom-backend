from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CartAPIView, CartItemViewSet

app_name = "cart"

router = DefaultRouter()
router.register("items", CartItemViewSet, basename="cart-item")

urlpatterns = [
    path("", CartAPIView.as_view(), name="cart-detail"),
]

urlpatterns += router.urls