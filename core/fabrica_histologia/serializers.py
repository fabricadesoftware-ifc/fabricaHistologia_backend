from core.fabrica_histologia.models import SlideMicroscopyPost, System 
from rest_framework import serializers

class SystemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields: list[str] = [
            "id",
            "name",
            "description",
            "image_system",
        ]

class SystemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields: list[str] = [
            "name",
            "description",
            "image_system",
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


