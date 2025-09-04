import django_filters
from core.posts.models import Posts, Point

class PostFilter(django_filters.FilterSet):
    organ_id = django_filters.NumberFilter(field_name="organ__id", lookup_expr='exact')
    species_id = django_filters.NumberFilter(field_name="species__id", lookup_expr='exact')
    type_post = django_filters.NumberFilter(field_name="type_post", lookup_expr='exact')
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    class Meta:
        model = Posts
        fields = ['organ_id', 'species_id', 'type_post', 'name']

class PointFilter(django_filters.FilterSet):
    posts_id = django_filters.NumberFilter(field_name="posts__id", lookup_expr='exact')
    id = django_filters.NumberFilter(field_name="id", lookup_expr='exact')
    label_title = django_filters.CharFilter(field_name="label_title", lookup_expr='icontains')
    class Meta:
        model =  Point
        fields = ['posts_id', 'id', 'label_title']