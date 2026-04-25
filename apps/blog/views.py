from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import selectors, services
from .serializers import (
    AddCommentSerializer,
    BlogCategorySerializer,
    CommentSerializer,
    PostDetailSerializer,
    PostListSerializer,
)


class BlogCategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = BlogCategorySerializer
    lookup_field = "slug"

    def get_queryset(self):
        return selectors.get_active_blog_categories()


class PostViewSet(ReadOnlyModelViewSet):
    lookup_field = "slug"

    def get_queryset(self):
        return selectors.get_published_posts()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer

        return PostListSerializer

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def add_comment(self, request, slug=None):
        post = self.get_object()

        serializer = AddCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            comment = services.add_comment(
                post=post,
                user=request.user,
                content=serializer.validated_data["content"],
            )
        except ValueError as error:
            return Response(
                {"detail": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        response_serializer = CommentSerializer(
            comment,
            context={"request": request},
        )
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)