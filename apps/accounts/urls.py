from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AddressViewSet, MyProfileAPIView

app_name = "accounts"

router = DefaultRouter()
router.register("addresses", AddressViewSet, basename="address")

urlpatterns = [
    path("me/", MyProfileAPIView.as_view(), name="my-profile"),
]

urlpatterns += router.urls