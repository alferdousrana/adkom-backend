from django.conf import settings
from django.db import models

from apps.core.models import BaseModel


class BlogCategory(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Blog categories"

    def __str__(self):
        return self.name


class Post(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    excerpt = models.TextField(blank=True)
    content = models.TextField()

    featured_image = models.ImageField(upload_to="blog/", null=True, blank=True)

    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_comments",
    )

    content = models.TextField()
    is_approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"