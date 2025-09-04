import django_filters
from .models import SupportingMaterial

class SupportingMaterialFilter(django_filters.FilterSet):
     system_id = django_filters.NumberFilter(field_name='system__id', lookup_expr='exact')
     name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
     class Meta:
        model = SupportingMaterial
        fields = ['system_id', 'name']