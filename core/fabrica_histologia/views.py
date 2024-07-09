from core.fabrica_histologia.serializers import SystemDetailSerializer, SystemWriteSerializer, speciesDetailSerializer, speciesWriteSerializer
from core.fabrica_histologia.models import System, Species
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

# Create your views here.

#System view

@extend_schema(tags=["System"])
class SystemViewSet(ModelViewSet):
    queryset = System.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SystemDetailSerializer
        return SystemWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

#Species view

@extend_schema(tags=["Species"])
class SpeciesViewSet(ModelViewSet):
    queryset = Species.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return speciesDetailSerializer
        return speciesWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]