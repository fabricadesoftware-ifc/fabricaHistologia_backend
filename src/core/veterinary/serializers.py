from rest_framework import serializers
from core.veterinary.models import System, Specie, Organ
from core.uploader.models import Image
from core.uploader.serializers import ImageSerializer

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
    image = serializers.SlugRelatedField(
        slug_field="attachment_key",
        queryset=Image.objects.all(),
        required=False,
        allow_null=True
    )
    class Meta:
        model = System
        fields: list[str] = [
            "name",
            "description",
            "image",
        ]



class SpecieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields: list[str] = [
            "id",
            "name",
            "category"
        ]

class SpecieWriteSerializer(serializers.ModelSerializer):
       class Meta:
        model = Specie
        fields: list[str] = [
            "name",
            "category"
        ]



class OrganWriteSerializer(serializers.ModelSerializer):
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