from rest_framework.routers import DefaultRouter

from core.supporting_materials.views import SupportingMaterialViewSet

router = DefaultRouter()

router.register(r"supporting-material", SupportingMaterialViewSet)