from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from passageidentity import Passage, PassageError
from passageidentity.openapi_client.models import UserInfo
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from core.user.models import User

PASSAGE_APP_ID = settings.PASSAGE_APP_ID
PASSAGE_API_KEY = settings.PASSAGE_API_KEY
PASSAGE_AUTH_STRATEGY = settings.PASSAGE_AUTH_STRATEGY
psg = Passage(PASSAGE_APP_ID, PASSAGE_API_KEY, auth_strategy=PASSAGE_AUTH_STRATEGY)


class TokenAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = "core.authentication.TokenAuthentication"
    name = "tokenAuth"
    match_subclasses = True
    priority = -1

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix="Bearer",
        )


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request) -> tuple[User, None] | None:
        if not request.headers.get("Authorization"):
            return None  # Sem token, não há autenticação

        try:
            # Obtendo o token do cabeçalho
            auth_header = request.headers.get("Authorization").split()
            print(f"header: {auth_header}")
            if len(auth_header) != 2 or auth_header[0].lower() != "bearer":
                raise AuthenticationFailed("Cabeçalho de autorização inválido")

            token = auth_header[1]
            print("Token recebido")
            
            try:
                psg_user_id: str = psg.validateJwt(token)
                print("Usuário autenticado:", psg_user_id)
            except (PassageError) as e:
                raise AuthenticationFailed("Erro na Valição do token", e)
            
            try:
                user = self._get_or_create_user(psg_user_id)
            except User.DoesNotExist:
                raise AuthenticationFailed("Usuário não encontrado")
            
            return (user, None)
        except (IndexError, PassageError) as e:
            raise AuthenticationFailed(f"Erro na autenticação: {str(e)}")
        
    def _get_or_create_user(self, psg_user_id) -> User:
        try:
            user: User = User.objects.get(passage_id=psg_user_id)
            print(user)
        except ObjectDoesNotExist:
            psg_user: UserInfo = psg.getUser(psg_user_id)
            user: User = User.objects.create_user(
                passage_id=psg_user.id,
                email=psg_user.email,
            )
        return user


    def _get_user_id(self, token) -> str:
        try:
            psg_user_id: str = psg.validateJwt(token)
        except PassageError as e:
            # print(e)
            raise AuthenticationFailed(e.message) from e

        return psg_user_id
