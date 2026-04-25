from rest_framework import serializers

from apps.product.models import Product
from apps.product.serializers import ProductListSerializer

from . import selectors
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = [
            "id",
            "product",
            "quantity",
            "created_at",
            "updated_at",
        ]


class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    item_count = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            "id",
            "items",
            "total",
            "item_count",
            "created_at",
            "updated_at",
        ]

    def get_items(self, obj):
        items = selectors.get_cart_items(obj)
        return CartItemSerializer(items, many=True, context=self.context).data

    def get_total(self, obj):
        return selectors.get_cart_total(obj)

    def get_item_count(self, obj):
        return selectors.get_cart_item_count(obj)


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1, default=1)

    def validate_product_id(self, value):
        product = Product.objects.filter(
            id=value,
            is_active=True,
            is_deleted=False,
        ).first()

        if not product:
            raise serializers.ValidationError("Product not found.")

        self.context["product"] = product
        return value


class UpdateCartItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)