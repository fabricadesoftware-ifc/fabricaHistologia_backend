from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField, PrimaryKeyRelatedField, DateField

from .models import User, PersonalData, Address


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AddressDetailSerializer(ModelSerializer):
    city = CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "A cidade é obrigatória.",
            "blank": "A cidade não pode ficar em branco."
        }
    )
    state = CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O estado é obrigatório.",
            "blank": "O estado não pode ficar em branco."
        }
    )

    class Meta:
        model = Address
        fields: list[str] = [
            "id",
            "city",
            "state",
        ]


class PersonalDataWriteSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field="email",
        queryset=User.objects.all(),
        required=True,
        error_messages={
            "required": "O usuário é obrigatório.",
            "does_not_exist": "Usuário inválido.",
            "incorrect_type": "Usuário inválido."
        }
    )
    name = CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O nome é obrigatório.",
            "blank": "O nome não pode ficar em branco."
        }
    )
    registration = CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "A matrícula é obrigatória.",
            "blank": "A matrícula não pode ficar em branco."
        }
    )
    birth_date = DateField(
        required=True,
        error_messages={
            "required": "A data de nascimento é obrigatória.",
            "invalid": "Data de nascimento inválida."
        }
    )
    phone = CharField(
        required=False,
        allow_blank=True
    )
    education_level = CharField(
        required=False,
        allow_blank=True
    )
    university = CharField(
        required=False,
        allow_blank=True
    )
    address = PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        required=False,
        allow_null=True,
        error_messages={
            "does_not_exist": "Endereço inválido.",
            "incorrect_type": "Endereço inválido."
        }
    )

    class Meta:
        model = PersonalData
        fields: list[str] = [
            "name",
            "registration",
            "birth_date",
            "phone",
            "education_level",
            "university",
            "user",
            "address",
        ]


class PersonalDataDetailSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    address = AddressDetailSerializer(read_only=True)

    class Meta:
        model = PersonalData
        fields: list[str] = [
            "id",
            "name",
            "registration",
            "birth_date",
            "phone",
            "education_level",
            "university",
            "user",
            "address",
        ]
        depth = 1


class PersonalDataListSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field="email",
        queryset=User.objects.all(),
        required=True,
        error_messages={
            "required": "O usuário é obrigatório.",
            "does_not_exist": "Usuário inválido.",
            "incorrect_type": "Usuário inválido."
        }
    )

    class Meta:
        model = PersonalData
        fields: list[str] = [
            "id",
            "name",
            "user",
            "registration",
            "birth_date",
            "phone",
            "education_level",
            "university",
            "address",
        ]
