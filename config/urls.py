from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/notifications/", include("apps.notification.urls")),
    path("api/products/", include("apps.product.urls")),
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/cart/", include("apps.cart.urls")),
    path("api/checkout/", include("apps.checkout.urls")),
]