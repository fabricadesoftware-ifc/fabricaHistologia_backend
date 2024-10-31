from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import User, PersonalData


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PersonalDataWriteSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    class Meta:
        model = PersonalData
        fields: list[str] = [
            "name",
            "registration",
            "birth_date",
            "phone",
            "education_level",
            "university",
            "user"
        ]

class PersonalDataDetailSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
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

class PersonalDataListSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
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