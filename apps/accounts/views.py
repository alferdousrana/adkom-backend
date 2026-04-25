from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from . import selectors, services
from .models import Address
from .serializers import AddressSerializer, ProfileSerializer


class MyProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = services.get_or_create_profile(request.user)
        serializer = ProfileSerializer(profile, context={"request": request})
        return Response(serializer.data)

    def patch(self, request):
        profile = services.update_profile(
            user=request.user,
            full_name=request.data.get("full_name"),
            phone=request.data.get("phone"),
            avatar=request.FILES.get("avatar"),
        )
        serializer = ProfileSerializer(profile, context={"request": request})
        return Response(serializer.data)


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return selectors.get_user_addresses(self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        address = self.get_object()
        services.delete_address(address)
        return Response(status=status.HTTP_204_NO_CONTENT)