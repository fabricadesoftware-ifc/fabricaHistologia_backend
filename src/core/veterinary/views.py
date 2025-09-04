from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from django_filters.rest_framework import DjangoFilterBackend

from core.veterinary.models import Organ, System, Specie
from core.veterinary.serializers import OrganDetailSerializer, OrganWriteSerializer
from core.veterinary.serializers import SystemDetailSerializer, SystemWriteSerializer
from core.veterinary.serializers import SpecieDetailSerializer, SpecieWriteSerializer
from core.veterinary.filters import OrganFilter, SystemFilter, SpecieFilter

@extend_schema(tags=["Organ"])
class OrganViewSet(ModelViewSet):
    queryset = Organ.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrganFilter 

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrganDetailSerializer
        return OrganWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

@extend_schema(tags=["System"])
class SystemViewSet(ModelViewSet):
    queryset = System.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SystemFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SystemDetailSerializer
        return SystemWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]


@extend_schema(tags=["Species"])
class SpeciesViewSet(ModelViewSet):
    queryset = Specie.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SpecieFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SpecieDetailSerializer
        return SpecieWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

