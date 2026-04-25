from .models import Cart, CartItem


def get_active_cart(user):
    return (
        Cart.objects.prefetch_related("items__product", "items__product__images")
        .filter(user=user, is_active=True, is_deleted=False)
        .first()
    )


def get_or_create_active_cart(user):
    cart = get_active_cart(user)

    if cart:
        return cart

    return Cart.objects.create(user=user)


def get_cart_items(cart):
    return CartItem.objects.select_related("product", "cart").prefetch_related(
        "product__images"
    ).filter(
        cart=cart,
        is_deleted=False,
    )


def get_cart_total(cart):
    total = 0

    for item in get_cart_items(cart):
        total += item.product.price * item.quantity

    return total


def get_cart_item_count(cart):
    return sum(item.quantity for item in get_cart_items(cart))