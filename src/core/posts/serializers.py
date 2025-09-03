from core.posts.models import Posts, Point
from core.uploader.models import Image
from core.uploader.serializers import ImageSerializer
from core.veterinary.models import Specie
from rest_framework import serializers


class PointRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields: list[str] = [
            "id",
            "label_title",
            "description",
            "position",
            "color",
            "posts",
            "analyzed_structures",
            "analyzed_functions",
        ]


class PointWriteSerializer(serializers.ModelSerializer):
    label_title = serializers.CharField(
        required=True,
        error_messages={
            "blank": "O campo 'Título' não pode ser vazio.",
            "required": "O campo 'Título' é obrigatório."
        }
    )
    description = serializers.CharField(
        required=True,
        error_messages={
            "blank": "A descrição é obrigatória.",
            "required": "Informe a descrição do ponto."
        }
    )
    position = serializers.CharField(
        required=True,
        error_messages={
            "blank": "A posição é obrigatória.",
            "required": "Informe a posição do ponto."
        }
    )
    color = serializers.CharField(
        required=True,
        error_messages={
            "blank": "A cor é obrigatória.",
            "required": "Informe a cor do ponto."
        }
    )
    posts = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Posts.objects.all(),
        required=True,
        error_messages={
            "required": "Você deve informar ao menos um post.",
            "does_not_exist": "Post informado não encontrado."
        }
    )
    analyzed_structures = serializers.CharField(
        required=False,
        allow_blank=True
    )
    analyzed_functions = serializers.CharField(
        required=False,
        allow_blank=True
    )

    class Meta:
        model = Point
        fields: list[str] = [
            "label_title",
            "description",
            "position",
            "color",
            "posts",
            "analyzed_structures",
            "analyzed_functions",
        ]


class PostsRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields: list[str] = [
            "id",
            "date_analysis",
            "post_date",
            "species",
            "type_cut",
            "increase",
            "coloring",
            "image",
            "autor_user",
            "organ",
            "type_post",
            "name"
        ]
        depth = 2


class PostsListSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = Posts
        fields: list[str] = [
            "id",
            "species",
            "image",
            "autor_user",
            "organ",
            "type_post",
            "increase",
            "type_cut",
            "name",
            "post_date"
        ]
        depth = 2


class PostsWriteSerializer(serializers.ModelSerializer):
    date_analysis = serializers.DateField(
        required=True,
        error_messages={
            "invalid": "Data de análise inválida.",
            "required": "Informe a data da análise."
        }
    )
    post_date = serializers.DateField(
        required=True,
        error_messages={
            "invalid": "Data de postagem inválida.",
            "required": "Informe a data de postagem."
        }
    )
    species = serializers.PrimaryKeyRelatedField(
    queryset=Specie.objects.all(),
    required=True,
    error_messages={
        "required": "O campo 'Espécie' é obrigatório.",
        "does_not_exist": "Espécie informada não encontrada."
    }
    )
    type_cut = serializers.CharField(
        required=True,
        error_messages={
            "blank": "O campo 'Tipo de Corte' é obrigatório.",
            "required": "Informe o tipo de corte."
        }
    )
    increase = serializers.CharField(
        required=True,
        error_messages={
            "blank": "O campo 'Aumento' é obrigatório.",
            "required": "Informe o aumento."
        }
    )
    coloring = serializers.CharField(
        required=True,
        error_messages={
            "blank": "O campo 'Coloração' é obrigatório.",
            "required": "Informe a coloração."
        }
    )
    image = serializers.SlugRelatedField(
        slug_field="attachment_key",
        queryset=Image.objects.all(),
        required=False,
        allow_null=True,
        error_messages={
            "does_not_exist": "A imagem informada não existe.",
            "invalid": "Imagem inválida."
        }
    )
    autor_user = serializers.PrimaryKeyRelatedField(
        queryset=Posts._meta.get_field('autor_user').related_model.objects.all(),
        required=True,
        error_messages={
            "required": "Informe o autor do post.",
            "does_not_exist": "O autor informado não foi encontrado."
        }
    )
    organ = serializers.PrimaryKeyRelatedField(
        queryset=Posts._meta.get_field('organ').related_model.objects.all(),
        required=True,
        error_messages={
            "required": "Informe o órgão relacionado.",
            "does_not_exist": "Órgão informado não encontrado."
        }
    )
    type_post = serializers.CharField(
        required=True,
        error_messages={
            "blank": "O campo 'Tipo de Post' é obrigatório.",
            "required": "Informe o tipo de post."
        }
    )
    name = serializers.CharField(
        required=True,
        error_messages={
            "blank": "O campo 'Nome' é obrigatório.",
            "required": "Informe o nome do post."
        }
    )

    class Meta:
        model = Posts
        fields: list[str] = [
            "date_analysis",
            "post_date",
            "species",
            "type_cut",
            "increase",
            "coloring",
            "image",
            "autor_user",
            "organ",
            "type_post",
            "name"
        ]
