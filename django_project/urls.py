from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from core.usuario.router import router as usuario_router
from core.usuario.views import verify_user
from core.uploader.router import router as uploader_router

from core.fabrica_histologia.views import PointViewSet, SpeciesViewSet, SystemViewSet, SlideMicroscopyPostViewSet
from core.quiz.views import AnswerViewSet, QuizViewSet

router = DefaultRouter()
router.register(r"species", SpeciesViewSet)
router.register(r"systems", SystemViewSet)
router.register(r"points", PointViewSet) 
router.register(r"Slide", SlideMicroscopyPostViewSet)
router.register(r"quiz", QuizViewSet)
router.register(r"answer", AnswerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/verify-user/<str:verification_token>/", verify_user, name="verify-user"),
    path("api/media/", include(uploader_router.urls)), 
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
