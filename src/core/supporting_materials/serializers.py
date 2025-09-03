from core.supporting_materials.models import SupportingMaterial
from core.uploader.models import Image, Document
from core.veterinary.models import System
from rest_framework import serializers

class SupportingMaterialDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportingMaterial
        fields: list[str] = [
            "id",
            "name",
            "description",
            "image_supporting_material",
            "document_supporting_material",
            "field_name",
            "system"
        ]
        depth = 2


class SupportingMaterialWriteSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O nome do material de apoio é obrigatório.",
            "blank": "O nome do material de apoio é obrigatório."
        }
    )
    description = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "A descrição do material de apoio é obrigatória.",
            "blank": "A descrição do material de apoio é obrigatória."
        }
    )
    field_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O campo é obrigatório.",
            "blank": "O campo é obrigatório."
        }
    )
    system = serializers.PrimaryKeyRelatedField(
        queryset=System.objects.all(),
        required=True,
        error_messages={
            "required": "O sistema é obrigatório.",
            "does_not_exist": "Sistema inválido.",
            "incorrect_type": "Sistema inválido."
        }
    )
    image_supporting_material = serializers.SlugRelatedField(
        slug_field="attachment_key",
        queryset=Image.objects.all(),
        required=False,
        allow_null=True
    )
    document_supporting_material = serializers.SlugRelatedField(
        slug_field="attachment_key",
        queryset=Document.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = SupportingMaterial
        fields: list[str] = [
            "name",
            "description",
            "image_supporting_material",
            "document_supporting_material",
            "field_name",
            "system"
        ]


class SupportingMaterialListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportingMaterial
        fields: list[str] = [
            "id",
            "name",
            "description",
            "field_name",
            "document_supporting_material",
            "image_supporting_material",
            "system"
        ]
        depth = 2
