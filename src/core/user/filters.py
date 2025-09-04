import django_filters
from core.user.models import PersonalData, Address, User

class PersonalDataFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name="user__id", lookup_expr='exact')
    user = django_filters.CharFilter(field_name="user", lookup_expr='icontains')
    class Meta:
        model = PersonalData
        fields = ['user_id', 'user']

class UserFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name="id", lookup_expr='exact')
    email = django_filters.CharFilter(field_name="email", lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['id', 'email']

class AddressFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name="city", lookup_expr='icontains')
    state = django_filters.CharFilter(field_name="state", lookup_expr='icontains')

    class Meta:
        model = Address
        fields = [ 'city', 'state',]
