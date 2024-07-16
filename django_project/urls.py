from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from core.usuario.router import router as usuario_router
from core.usuario.views import verify_user
from core.uploader.router import router as uploader_router

from core.fabrica_histologia.views import PointViewSet, SpeciesViewSet, SystemViewSet, SlideMicroscopyPostViewSet, verify_slide_microscopy_post
from core.quiz.views import AnswerViewSet, QuizViewSet
from core.supporting_materials.views import SupportingMaterialViewSet

router = DefaultRouter()
router.register(r"species", SpeciesViewSet)
router.register(r"systems", SystemViewSet)
router.register(r"points", PointViewSet) 
router.register(r"slide", SlideMicroscopyPostViewSet)
router.register(r"quiz", QuizViewSet)
router.register(r"answer", AnswerViewSet)
router.register(r"supporting-material", SupportingMaterialViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/verify-user/<str:verification_token>/", verify_user, name="verify-user"),
    path("api/verify-post/<str:verification_token>/", verify_slide_microscopy_post, name="verify-post"),
    path("api/media/", include(uploader_router.urls)), 
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
