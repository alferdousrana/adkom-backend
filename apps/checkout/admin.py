from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_amount", "is_paid", "is_cancelled", "created_at")
    list_filter = ("is_paid", "is_cancelled", "created_at")
    search_fields = ("user__username", "user__email", "full_name", "phone")
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "price", "quantity", "created_at")
    search_fields = ("order__user__username", "order__user__email", "product__name")