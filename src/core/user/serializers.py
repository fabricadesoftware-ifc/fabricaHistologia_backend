from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import User, PersonalData, Address


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AddressDetailSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields: list[str] = [
            "id",
            "city", 
            "state",
        ]

class AddressWriteSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields: list[str] = [
            "city", 
            "state",
        ]

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
            "user",
            "address",
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
            "user",
            "address",
        ]
        depth = 1

class PersonalDataListSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field="email", queryset=User.objects.all())
    class Meta:
        model = PersonalData
        fields: list[str] = [
            "id",
            "name",
            "user",
            "registration",
            "birth_date",
            "phone",
            "education_level",
            "university",
            "address",
        ]