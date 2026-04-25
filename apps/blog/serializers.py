from rest_framework import serializers

from . import selectors
from .models import BlogCategory, Comment, Post


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = [
            "id",
            "name",
            "slug",
        ]


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "username",
            "content",
            "created_at",
        ]


class PostListSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "category",
            "author",
            "title",
            "slug",
            "excerpt",
            "featured_image",
            "published_at",
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)
    author = serializers.CharField(source="author.username", read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "category",
            "author",
            "title",
            "slug",
            "excerpt",
            "content",
            "featured_image",
            "published_at",
            "comments",
            "created_at",
            "updated_at",
        ]

    def get_comments(self, obj):
        comments = selectors.get_approved_comments(obj)
        return CommentSerializer(comments, many=True, context=self.context).data


class AddCommentSerializer(serializers.Serializer):
    content = serializers.CharField()