import django_filters
from core.posts.models import Posts

class PostFilter(django_filters.FilterSet):
    organ_id = django_filters.NumberFilter(field_name="organ__id", lookup_expr='exact')
    species_id = django_filters.NumberFilter(field_name="species__id", lookup_expr='exact')


    class Meta:
        model = Posts
        fields = ['organ_id', 'species_id']