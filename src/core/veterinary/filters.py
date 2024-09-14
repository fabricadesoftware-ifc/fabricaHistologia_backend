import django_filters
from core.veterinary.models import Organ

class OrganFilter(django_filters.FilterSet):
    system_id = django_filters.NumberFilter(field_name='system__id', lookup_expr='icontains')

    class Meta:
        model = Organ
        fields = ['system_id']
