from core.fabrica_histologia.models import System, Point, Specie, SlideMicroscopyPost
from core.fabrica_histologia.serializers import SystemDetailSerializer, SystemWriteSerializer
from core.fabrica_histologia.serializers import PointDetailSerializer, PointWriteSerializer
from core.fabrica_histologia.serializers import SpecieDetailSerializer, SpecieWriteSerializer
from core.fabrica_histologia.serializers import SlideMicroscopyPostWriteSerializer, SlideMicroscopyPostListSerializer, SlideMicroscopyPostDetailSerializer

from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

#System view

@extend_schema(tags=["System"])
class SystemViewSet(ModelViewSet):
    queryset = System.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SystemDetailSerializer
        return SystemWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

class PointViewSet(ModelViewSet):
    queryset = Point.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PointDetailSerializer
        return PointWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

@extend_schema(tags=["Species"])
class SpeciesViewSet(ModelViewSet):
    queryset = Specie.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SpecieDetailSerializer
        return SpecieWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

@extend_schema(tags=["SlideMicroscopyPost"])
class SlideMicroscopyPostViewSet(ModelViewSet):
    queryset = SlideMicroscopyPost.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list"]:            
            return SlideMicroscopyPostListSerializer
        elif self.action in ["retrieve"]:
            return SlideMicroscopyPostDetailSerializer
        return SlideMicroscopyPostWriteSerializer
    http_method_names = ["get", "post", "put", "delete"]

@api_view(['GET'])
def verify_slide_microscopy_post(request, verification_token):
    try:
        post  = SlideMicroscopyPost.objects.get(verification_token=verification_token)
    except SlideMicroscopyPost.DoesNotExist:
        return Response({'error': 'Token de verificação inválido'}, status=status.HTTP_404_NOT_FOUND)

    # Marcar o usuário como verificado
    post.is_verified = True
    post.verification_token = None  # Limpar o token após verificação
    post.save()

    return Response({'message': 'Postagem verificada com sucesso'}, status=status.HTTP_200_OK)
