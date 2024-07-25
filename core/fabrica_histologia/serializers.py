from rest_framework import serializers
from core.fabrica_histologia.models import System, Specie, Point, SlideMicroscopyPost, Organ

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
        model = Point
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
        model = Point
        fields: list[str] = [
             "label_title",
             "description",
             "position",
             "color",
             "slide",
             "analyzed_structures",
             "analyzed_functions",
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

class OrganWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organ 
        fields: list[str] = [
            "name",
            "description",
            "image_organ",
            "system",
        ]

class OrganDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organ 
        fields: list[str] = [
            "id",
            "name",
            "description",
            "image_organ",
            "system",
        ]