from rest_framework.viewsets import ReadOnlyModelViewSet

from . import selectors
from .models import Category, Product
from .serializers import CategorySerializer, ProductDetailSerializer, ProductListSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    lookup_field = "slug"

    def get_queryset(self):
        return selectors.get_active_categories()


class ProductViewSet(ReadOnlyModelViewSet):
    lookup_field = "slug"

    def get_queryset(self):
        return selectors.get_active_products()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductDetailSerializer

        return ProductListSerializer