from .models import Product


def update_product_stock(*, product, quantity):
    product.stock = quantity
    product.save(update_fields=["stock", "updated_at"])
    return product


def decrease_product_stock(*, product, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if product.stock < quantity:
        raise ValueError("Not enough stock available.")

    product.stock -= quantity
    product.save(update_fields=["stock", "updated_at"])
    return product


def increase_product_stock(*, product, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    product.stock += quantity
    product.save(update_fields=["stock", "updated_at"])
    return product


def deactivate_product(product):
    product.is_active = False
    product.save(update_fields=["is_active", "updated_at"])
    return product