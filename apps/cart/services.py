from . import selectors
from .models import CartItem


def add_to_cart(*, user, product, quantity=1):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if not product.is_active or product.is_deleted:
        raise ValueError("Product is not available.")

    if product.stock < quantity:
        raise ValueError("Not enough stock available.")

    cart = selectors.get_or_create_active_cart(user)

    cart_item = CartItem.objects.filter(
        cart=cart,
        product=product,
        is_deleted=False,
    ).first()

    if cart_item:
        new_quantity = cart_item.quantity + quantity

        if product.stock < new_quantity:
            raise ValueError("Not enough stock available.")

        cart_item.quantity = new_quantity
        cart_item.save(update_fields=["quantity", "updated_at"])
        return cart_item

    return CartItem.objects.create(
        cart=cart,
        product=product,
        quantity=quantity,
    )


def update_cart_item_quantity(*, cart_item, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if cart_item.product.stock < quantity:
        raise ValueError("Not enough stock available.")

    cart_item.quantity = quantity
    cart_item.save(update_fields=["quantity", "updated_at"])
    return cart_item


def remove_cart_item(cart_item):
    cart_item.soft_delete()
    return cart_item


def clear_cart(cart):
    selectors.get_cart_items(cart).update(is_deleted=True)
    return cart


def deactivate_cart(cart):
    cart.is_active = False
    cart.save(update_fields=["is_active", "updated_at"])
    return cart