from core.supporting_materials.models import SupportingMaterial
from core.supporting_materials.serializers import SupportingMaterialDetailSerializer, SupportingMaterialWriteSerializer, SupportingMaterialListSerializer
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

class SupportingMaterialViewSet(ModelViewSet):
    queryset = SupportingMaterial.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list"]:            
            return SupportingMaterialListSerializer
        elif self.action in ["retrieve"]:
            return SupportingMaterialDetailSerializer
        return SupportingMaterialWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]