from rest_framework.routers import DefaultRouter

from core.veterinary.views import OrganViewSet, SpeciesViewSet, SystemViewSet

router = DefaultRouter()

router.register(r"organs", OrganViewSet)
router.register(r"species", SpeciesViewSet)
router.register(r"systems", SystemViewSet)