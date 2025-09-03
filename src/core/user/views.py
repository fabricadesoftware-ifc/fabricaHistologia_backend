from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_project.permissions import customVerifiedPermission, customDataPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from django_filters.rest_framework import DjangoFilterBackend

from core.user.models import User, PersonalData, Address
from core.user.serializers import UserSerializer, PersonalDataWriteSerializer, PersonalDataDetailSerializer, PersonalDataListSerializer, AddressDetailSerializer
from core.user.filters import PersonalDataFilter

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    permission_classes = [customVerifiedPermission]

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer
    permission_classes = [IsAuthenticated]

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


class PersonalDataViewSet(ModelViewSet):
    queryset = PersonalData.objects.all().order_by("id")
    serializer_class = PersonalDataWriteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PersonalDataFilter
    permission_classes = [customDataPermission]

    def get_serializer_class(self):
        if self.action in ["list"]:
            return PersonalDataListSerializer
        elif self.action in ["retrieve"]:
            return PersonalDataDetailSerializer
        return PersonalDataWriteSerializer
    
