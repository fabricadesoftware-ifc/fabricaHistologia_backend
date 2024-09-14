import django_filters
from core.veterinary.models import Organ

class OrganFilter(django_filters.FilterSet):
    system_name = django_filters.CharFilter(field_name='system__name', lookup_expr='icontains')

    class Meta:
        model = Organ
        fields = ['system_name']
