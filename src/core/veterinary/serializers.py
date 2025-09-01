from rest_framework import serializers
from core.veterinary.models import System, Specie, Organ
from core.uploader.models import Image
from core.uploader.serializers import ImageSerializer

# ------------------- SYSTEM SERIALIZERS -------------------

class SystemDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = System
        fields: list[str] = [
            "id",
            "name",
            "description",
            "image",
        ]


class SystemWriteSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O nome do sistema é obrigatório.",
            "blank": "O nome do sistema é obrigatório."
        }
    )
    description = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "A descrição do sistema é obrigatória.",
            "blank": "A descrição do sistema é obrigatória."
        }
    )
    image = serializers.SlugRelatedField(
        slug_field="attachment_key",
        queryset=Image.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = System
        fields: list[str] = [
            "id",
            "name",
            "description",
            "image",
        ]

# ------------------- SPECIE SERIALIZERS -------------------

class SpecieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields: list[str] = [
            "id",
            "name",
            "category"
        ]


class SpecieWriteSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O nome da espécie é obrigatório.",
            "blank": "O nome da espécie é obrigatório."
        }
    )
    category = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "A categoria da espécie é obrigatória.",
            "blank": "A categoria da espécie é obrigatória."
        }
    )

    class Meta:
        model = Specie
        fields: list[str] = [
            "name",
            "category"
        ]

# ------------------- ORGAN SERIALIZERS -------------------

class OrganWriteSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O nome do órgão é obrigatório.",
            "blank": "O nome do órgão é obrigatório."
        }
    )
    description = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "A descrição do órgão é obrigatória.",
            "blank": "A descrição do órgão é obrigatória."
        }
    )
    system = serializers.PrimaryKeyRelatedField(
        queryset=System.objects.all(),
        required=True,
        error_messages={
            "required": "O sistema do órgão é obrigatório.",
            "does_not_exist": "Sistema inválido.",
            "incorrect_type": "Sistema inválido."
        }
    )
    image = serializers.SlugRelatedField(
        slug_field="attachment_key",
        queryset=Image.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Organ
        fields: list[str] = [
            "name",
            "description",
            "image",
            "system",
        ]


class OrganDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = Organ
        fields: list[str] = [
            "id",
            "name",
            "description",
            "image",
            "system",
        ]
        depth = 2
