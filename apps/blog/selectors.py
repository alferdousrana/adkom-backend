from .models import BlogCategory, Comment, Post


def get_active_blog_categories():
    return BlogCategory.objects.filter(
        is_active=True,
        is_deleted=False,
    )


def get_published_posts():
    return (
        Post.objects.select_related("author", "category")
        .prefetch_related("comments")
        .filter(
            is_published=True,
            is_deleted=False,
        )
    )


def get_post_detail(*, slug):
    return get_published_posts().filter(slug=slug).first()


def get_posts_by_category(*, category_slug):
    return get_published_posts().filter(
        category__slug=category_slug,
        category__is_active=True,
        category__is_deleted=False,
    )


def get_author_posts(*, author):
    return get_published_posts().filter(author=author)


def get_approved_comments(post):
    return Comment.objects.select_related("user", "post").filter(
        post=post,
        is_approved=True,
        is_deleted=False,
    )