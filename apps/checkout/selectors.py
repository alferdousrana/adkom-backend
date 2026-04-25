from .models import Order


def get_user_orders(user):
    return Order.objects.prefetch_related("items__product", "items__product__images").filter(
        user=user,
        is_deleted=False,
    )


def get_order_detail(*, user, order_id):
    return get_user_orders(user).filter(id=order_id).first()


def get_pending_orders(user):
    return get_user_orders(user).filter(
        is_paid=False,
        is_cancelled=False,
    )