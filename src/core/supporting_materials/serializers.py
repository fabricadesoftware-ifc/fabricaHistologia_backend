from core.supporting_materials.models import SupportingMaterial
from core.uploader.models import Image, Document
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
            "name",
            "description",
            "field_name",
            "document_supporting_material",
            "image_supporting_material",
            "system"
        ]

        depth = 2