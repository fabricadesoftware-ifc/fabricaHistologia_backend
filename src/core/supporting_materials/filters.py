import django_filters
from .models import SupportingMaterial

class SupportingMaterialFilter(django_filters.FilterSet):
     system_id = django_filters.NumberFilter(field_name='system__id', lookup_expr='exact')

     class Meta:
        model = SupportingMaterial
        fields = ['system_id']