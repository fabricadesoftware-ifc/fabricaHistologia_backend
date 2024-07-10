from core.fabrica_histologia.serializers import SystemDetailSerializer, SystemWriteSerializer, PointDetailSerializer, PointWriteSerializer
from core.fabrica_histologia.models import System
from core.fabrica_histologia.models import Points
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

# Create your views here.

@extend_schema(tags=["System"])
class SystemViewSet(ModelViewSet):
    queryset = System.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SystemDetailSerializer
        return SystemWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

class PointViewSet(ModelViewSet):
    queryset = Points.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PointDetailSerializer
        return PointWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

    