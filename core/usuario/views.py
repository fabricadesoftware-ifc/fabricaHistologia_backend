from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from core.usuario.models import Usuario as User
from core.usuario.serializers import UsuarioSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UsuarioSerializer


    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = UsuarioSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def verify_user(request, verification_token):
    try:
        user = User.objects.get(verification_token=verification_token)
    except User.DoesNotExist:
        return Response({'error': 'Token de verificação inválido'}, status=status.HTTP_404_NOT_FOUND)

    # Marcar o usuário como verificado
    user.is_verified = True
    user.verification_token = None  # Limpar o token após verificação
    user.save()

    return Response({'message': 'Usuário verificado com sucesso'}, status=status.HTTP_200_OK)