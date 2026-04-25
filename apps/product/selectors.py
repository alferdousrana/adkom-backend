from .models import Category, Product


def get_active_categories():
    return Category.objects.filter(
        is_active=True,
        is_deleted=False,
    )


def get_active_products():
    return Product.objects.select_related("category").prefetch_related("images").filter(
        is_active=True,
        is_deleted=False,
        category__is_active=True,
        category__is_deleted=False,
    )


def get_product_detail(*, slug):
    return get_active_products().filter(slug=slug).first()


def get_products_by_category(*, category_slug):
    return get_active_products().filter(category__slug=category_slug)


def get_low_stock_products(*, limit=5):
    return get_active_products().filter(stock__lte=limit)