from django.db import transaction

from apps.cart import selectors as cart_selectors
from apps.cart import services as cart_services
from apps.product import services as product_services

from .models import Order, OrderItem


def calculate_cart_total(cart):
    return cart_selectors.get_cart_total(cart)


@transaction.atomic
def create_order_from_cart(*, user, address):
    cart = cart_selectors.get_active_cart(user)

    if not cart:
        raise ValueError("No active cart found.")

    cart_items = list(cart_selectors.get_cart_items(cart))

    if not cart_items:
        raise ValueError("Cart is empty.")

    total_amount = calculate_cart_total(cart)

    order = Order.objects.create(
        user=user,
        full_name=address.full_name,
        phone=address.phone,
        address_line=address.address_line,
        city=address.city,
        postal_code=address.postal_code,
        total_amount=total_amount,
    )

    for cart_item in cart_items:
        if cart_item.product.stock < cart_item.quantity:
            raise ValueError(f"Not enough stock for {cart_item.product.name}.")

        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            price=cart_item.product.price,
            quantity=cart_item.quantity,
        )

        product_services.decrease_product_stock(
            product=cart_item.product,
            quantity=cart_item.quantity,
        )

    cart_services.clear_cart(cart)
    cart_services.deactivate_cart(cart)

    return order


def mark_order_paid(order):
    if order.is_cancelled:
        raise ValueError("Cancelled order cannot be marked as paid.")

    order.is_paid = True
    order.save(update_fields=["is_paid", "updated_at"])
    return order


def cancel_order(order):
    if order.is_paid:
        raise ValueError("Paid order cannot be cancelled.")

    order.is_cancelled = True
    order.save(update_fields=["is_cancelled", "updated_at"])
    return order