from django.contrib import admin

from .models import BlogCategory, Comment, Post


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "is_published", "published_at")
    list_filter = ("is_published", "category", "created_at", "published_at")
    search_fields = ("title", "slug", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at")
    search_fields = ("post__title", "user__username", "user__email", "content")