import django_filters
from core.veterinary.models import Organ, Specie, System

class OrganFilter(django_filters.FilterSet):
    system_id = django_filters.NumberFilter(field_name='system__id', lookup_expr='exact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Organ
        fields = ['system_id', 'name']

class SpecieFilter(django_filters.FilterSet):
    system_id = django_filters.NumberFilter(field_name='system__id', lookup_expr='exact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Specie
        fields = ['system_id', 'name']

class SystemFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = System
        fields = ['id', 'name']


