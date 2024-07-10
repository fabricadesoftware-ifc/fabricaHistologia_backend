from rest_framework import serializers
from core.fabrica_histologia.models import System, Species, Points, SlideMicroscopyPost

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


class PointDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields: list[str] = [
            "id",
             "label_title",
             "description",
             "position",
             "color",
             "slide",
             "analyzed_structures",
             "analyzed_functions",
        ] 

class PointWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields: list[str] = [
             "label_title",
             "description",
             "position",
             "color",
             "slide",
             "analyzed_structures",
             "analyzed_functions",
        ] 

class SpeciesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields: list[str] = [
            "id",
            "name",
            "category"
        ]

class SpeciesWriteSerializer(serializers.ModelSerializer):
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

