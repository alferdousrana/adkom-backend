from django.utils import timezone

from .models import Comment, Post


def publish_post(post):
    if post.is_published:
        return post

    post.is_published = True
    post.published_at = timezone.now()
    post.save(update_fields=["is_published", "published_at", "updated_at"])
    return post


def unpublish_post(post):
    if not post.is_published:
        return post

    post.is_published = False
    post.published_at = None
    post.save(update_fields=["is_published", "published_at", "updated_at"])
    return post


def add_comment(*, post, user, content):
    if not content:
        raise ValueError("Comment content is required.")

    return Comment.objects.create(
        post=post,
        user=user,
        content=content,
    )


def approve_comment(comment):
    comment.is_approved = True
    comment.save(update_fields=["is_approved", "updated_at"])
    return comment


def delete_comment(comment):
    comment.soft_delete()
    return comment