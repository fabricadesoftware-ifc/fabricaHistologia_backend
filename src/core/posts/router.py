from rest_framework.routers import DefaultRouter

from core.posts.views import PointViewSet, PostsViewSet

router = DefaultRouter()

router.register(r"points", PointViewSet)
router.register(r"posts", PostsViewSet)

