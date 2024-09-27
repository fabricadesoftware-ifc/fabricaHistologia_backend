from core.supporting_materials.models import SupportingMaterial
from core.supporting_materials.serializers import SupportingMaterialDetailSerializer, SupportingMaterialWriteSerializer, SupportingMaterialListSerializer

from core.supporting_materials.filters import SupportingMaterialFilter
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend


class SupportingMaterialViewSet(ModelViewSet):
    queryset = SupportingMaterial.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupportingMaterialFilter
    
    def get_serializer_class(self):
        if self.action in ["list"]:            
            return SupportingMaterialListSerializer
        elif self.action in ["retrieve"]:
            return SupportingMaterialDetailSerializer
        return SupportingMaterialWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]