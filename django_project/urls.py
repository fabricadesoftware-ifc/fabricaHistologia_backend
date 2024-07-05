"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from core.usuario.router import router as usuario_router
from core.usuario.views import verify_user
from core.fabrica_histologia.views import SlideMicroscopyPostViewSet
from core.uploader.router import router as uploader_router

router = DefaultRouter()
router.register(r"slides", SlideMicroscopyPostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/fabrica-histologia/', include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/verify-user/<str:verification_token>/", verify_user, name="verify-user"),
    path("api/media/", include(uploader_router.urls)), 
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
