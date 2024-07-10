
from core.fabrica_histologia.models import System, Species
from core.fabrica_histologia.models import SlideMicroscopyPost, System 
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

class SlideMicroscopyPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideMicroscopyPost
        fields: list[str] = [
            "id",
            "date_analysis",
            "post_date",
            "species",
            "type_cut",
            "increase",
            "coloring",
            "image_slide",
            "autor_user",
            "organ",
        ]
        depth = 1

class SlideMicroscopyPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model: SlideMicroscopyPost
        fields: list[str] = [
            "species",
            "image_slide",
            "autor_user",
            "organ",
        ]
        depth = 1

class SlideMicroscopyPostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideMicroscopyPost
        fields: list[str] = [
            "date_analysis",
            "post_date",
            "species",
            "type_cut",
            "increase",
            "coloring",
            "image_slide",
            "autor_user",
            "organ",
        ]
        depth = 1
