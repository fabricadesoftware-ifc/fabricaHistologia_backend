from rest_framework.routers import DefaultRouter

from core.posts.router import router as posts_router
from core.supporting_materials.router import router as supporting_materials_router
from core.quiz.router import router as quiz_router
from core.veterinary.router import router as veterinary_router
from core.uploader.router import router as uploader_router
from core.user.router import router as users_router

router = DefaultRouter()
router.registry.extend(posts_router.registry)
router.registry.extend(supporting_materials_router.registry)
router.registry.extend(quiz_router.registry)
router.registry.extend(veterinary_router.registry)
router.registry.extend(uploader_router.registry)
router.registry.extend(users_router.registry)

