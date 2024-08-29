from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from core.veterinary.models import Organ, System, Specie
from core.veterinary.serializers import OrganDetailSerializer, OrganWriteSerializer
from core.veterinary.serializers import SystemDetailSerializer, SystemWriteSerializer
from core.veterinary.serializers import SpecieDetailSerializer, SpecieWriteSerializer

@extend_schema(tags=["Organ"])
class OrganViewSet(ModelViewSet):
    queryset = Organ.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrganDetailSerializer
        return OrganWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

@extend_schema(tags=["System"])
class SystemViewSet(ModelViewSet):
    queryset = System.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SystemDetailSerializer
        return SystemWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]


@extend_schema(tags=["Species"])
class SpeciesViewSet(ModelViewSet):
    queryset = Specie.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SpecieDetailSerializer
        return SpecieWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

