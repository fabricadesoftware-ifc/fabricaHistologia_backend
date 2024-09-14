from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from core.posts.models import Posts, Point
from core.posts.serializers import PointRetriveSerializer, PointWriteSerializer
from core.posts.serializers import PostsWriteSerializer, PostsListSerializer, PostsRetriveSerializer
from core.posts.filters import PostFilter

@extend_schema(tags=["Posts"])
class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    
    def get_serializer_class(self):
        if self.action in ["list"]:            
            return PostsListSerializer
        elif self.action in ["retrieve"]:
            return PostsRetriveSerializer
        return PostsWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

@extend_schema(tags=["Point"])
class PointViewSet(ModelViewSet):
    queryset = Point.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PointRetriveSerializer
        return PointWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]



@api_view(['GET'])
def verify_slide_microscopy_post(request, verification_token):
    try:
        post  = Posts.objects.get(verification_token=verification_token)
    except Posts.DoesNotExist:
        return Response({'error': 'Token de verificação inválido'}, status=status.HTTP_404_NOT_FOUND)

    # Marcar o usuário como verificado
    post.is_verified = True
    post.verification_token = None  # Limpar o token após verificação
    post.save()

    return Response({'message': 'Postagem verificada com sucesso'}, status=status.HTTP_200_OK)
