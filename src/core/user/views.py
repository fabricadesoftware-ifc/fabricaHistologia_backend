from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_project.permissions import customVerifiedPermission, customDataPermission
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from django_filters.rest_framework import DjangoFilterBackend

from core.user.models import User, PersonalData, Address
from core.user.serializers import UserSerializer, PersonalDataWriteSerializer, PersonalDataDetailSerializer, PersonalDataListSerializer, AddressDetailSerializer, UserRegistrationSerializer
from core.user.filters import PersonalDataFilter, UserFilter, AddressFilter
from tasks.recover_password_code import recover_password_code

import secrets

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    permission_classes = [customVerifiedPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_serializer_class(self):
        if self.action == "register":
            return UserRegistrationSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == "register":
            return []
        return super().get_permissions()

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], permission_classes=[])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"message": "Usuário criado com sucesso", "email": user.email},
            status=status.HTTP_201_CREATED,
        )
    
    @action(detail=False, methods=["post"], permission_classes=[])
    def forget(self, request):
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        user.recover_password_token = ''.join(str(secrets.randbelow(10)) for _ in range(4))
        user.save()
        
        recover_password_code.delay(user.id, user.recover_password_token)
        
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["post"], permission_classes=[])
    def recover(self, request):
        email = request.data.get("email")
        code = request.data.get("code")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        if user.recover_password_token != code or user.recover_password_token is None:
            return Response({'error': 'Código de recuperação de senha inválido'}, status=status.HTTP_400_BAD_REQUEST)

        password = request.data.get("password")
        
        if not password:
            return Response({'error': 'A senha é obrigatória'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            validate_password(password)
        except ValidationError as e:
            return Response(
                {"error": e.messages},
                status=status.HTTP_400_BAD_REQUEST
            )        
            
        user.set_password(password)
        
        user.recover_password_token = None
        user.save()
        
        return Response(status=status.HTTP_200_OK)

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AddressFilter

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
    
