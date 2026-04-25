from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import selectors, services
from .serializers import AddToCartSerializer, CartItemSerializer, CartSerializer, UpdateCartItemSerializer


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = selectors.get_or_create_active_cart(request.user)
        serializer = CartSerializer(cart, context={"request": request})
        return Response(serializer.data)


class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["post", "patch", "delete", "head", "options"]

    def get_queryset(self):
        cart = selectors.get_or_create_active_cart(self.request.user)
        return selectors.get_cart_items(cart)

    def create(self, request, *args, **kwargs):
        serializer = AddToCartSerializer(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)

        cart_item = services.add_to_cart(
            user=request.user,
            product=serializer.context["product"],
            quantity=serializer.validated_data["quantity"],
        )

        response_serializer = CartItemSerializer(
            cart_item,
            context={"request": request},
        )
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        cart_item = self.get_object()

        serializer = UpdateCartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart_item = services.update_cart_item_quantity(
            cart_item=cart_item,
            quantity=serializer.validated_data["quantity"],
        )

        response_serializer = CartItemSerializer(
            cart_item,
            context={"request": request},
        )
        return Response(response_serializer.data)

    def destroy(self, request, *args, **kwargs):
        cart_item = self.get_object()
        services.remove_cart_item(cart_item)
        return Response(status=status.HTTP_204_NO_CONTENT)