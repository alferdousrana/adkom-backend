from rest_framework import serializers

from apps.accounts.models import Address
from apps.product.serializers import ProductListSerializer

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "price",
            "quantity",
            "created_at",
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "full_name",
            "phone",
            "address_line",
            "city",
            "postal_code",
            "total_amount",
            "is_paid",
            "is_cancelled",
            "items",
            "created_at",
            "updated_at",
        ]


class CheckoutSerializer(serializers.Serializer):
    address_id = serializers.IntegerField()

    def validate_address_id(self, value):
        request = self.context["request"]

        address = Address.objects.filter(
            id=value,
            user=request.user,
            is_deleted=False,
        ).first()

        if not address:
            raise serializers.ValidationError("Address not found.")

        self.context["address"] = address
        return value