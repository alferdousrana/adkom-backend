from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CheckoutAPIView, OrderViewSet

app_name = "checkout"

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="order")

urlpatterns = [
    path("", CheckoutAPIView.as_view(), name="checkout"),
]

urlpatterns += router.urls