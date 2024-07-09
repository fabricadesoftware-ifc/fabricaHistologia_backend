from core.fabrica_histologia.models import System, Species
from rest_framework import serializers

# Create your serializers here

# System serializer for listing methods

class SystemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields: list[str] = [
            "id",
            "name",
            "description",
            "image_system",
        ]

# System serializer for posting methods

class SystemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields: list[str] = [
            "name",
            "description",
            "image_system",
        ]

# Species serializer for listing methods

class speciesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields: list[str] = [
            "id",
            "name",
            "category"
        ]

# Species serializer for posting methods

class speciesWriteSerializer(serializers.ModelSerializer):
       class Meta:
        model = Species
        fields: list[str] = [
            "name",
            "category"
        ]