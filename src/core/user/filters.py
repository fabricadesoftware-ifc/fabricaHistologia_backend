import django_filters
from core.user.models import PersonalData

class PersonalDataFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name="user__id", lookup_expr='exact')

    class Meta:
        model = PersonalData
        fields = ['user_id']