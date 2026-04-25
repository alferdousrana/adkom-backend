from rest_framework.routers import DefaultRouter

from .views import BlogCategoryViewSet, PostViewSet

app_name = "blog"

router = DefaultRouter()
router.register("categories", BlogCategoryViewSet, basename="blog-category")
router.register("", PostViewSet, basename="post")

urlpatterns = router.urls