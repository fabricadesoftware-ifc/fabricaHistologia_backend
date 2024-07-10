from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Usuario, PersonalData


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class PersonalDataWriteSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=Usuario.objects.all())
    class Meta:
        model = PersonalData
        fields: list[str] = [
            "name",
            "registration",
            "birth_date",
            "phone",
            "education_level",
            "university"
        ]

class PersonalDataDetailSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=Usuario.objects.all())
    class Meta:
        model = PersonalData
        fields: list[str] = [
            "id",
            "name",
            "registration",
            "birth_date",
            "phone",
            "education_level",
            "university"
        ]

class PersonalDataListSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=Usuario.objects.all())
    class Meta:
        model = PersonalData
        fields: list[str] = [
            "id",
            "name",
            "registration",
            "birth_date",
            "phone",
            "education_level",
            "university",
            "user"
        ]