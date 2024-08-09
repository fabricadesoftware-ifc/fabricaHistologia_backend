from core.supporting_materials.models import SupportingMaterial
from rest_framework.serializers import ModelSerializer

class SupportingMaterialDetailSerializer(ModelSerializer):
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

class SupportingMaterialWriteSerializer(ModelSerializer):
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

class SupportingMaterialListSerializer(ModelSerializer):
    class Meta:
        model = SupportingMaterial
        fields: list[str] = [
            "name",
            "description",
            "field_name",
            "system"
        ]