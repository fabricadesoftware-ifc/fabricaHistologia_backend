from rest_framework import serializers
from core.veterinary.models import System, Specie, Organ

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