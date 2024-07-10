from core.fabrica_histologia.models import System
from core.fabrica_histologia.models import Points
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

