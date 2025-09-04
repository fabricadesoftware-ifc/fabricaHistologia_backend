from rest_framework import serializers
from core.quiz.models import Quiz, Answer, Score
from core.veterinary.models import System
from core.user.models import User

# ------------------- QUIZ SERIALIZERS -------------------

class QuizDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields: list[str] = [
            "id",
            "title",
            "question",
            "level",
            "system"
        ]
        depth = 2


class QuizWriteSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        required=False,
        allow_blank=True,
       
    )
    question = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "A pergunta do quiz é obrigatória.",
            "blank": "A pergunta do quiz não pode ficar em branco."
        }
    )
    level = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O nível do quiz é obrigatório.",
            "blank": "O nível do quiz não pode ficar em branco."
        }
    )
    system = serializers.PrimaryKeyRelatedField(
        queryset=System.objects.all(),  # <<< importante
        required=True,
        error_messages={
            "required": "O sistema é obrigatório.",
            "does_not_exist": "Sistema inválido.",
            "incorrect_type": "Sistema inválido."
        }
    )

    class Meta:
        model = Quiz
        fields: list[str] = [
            "title",
            "question",
            "level",
            "system"
        ]


# ------------------- ANSWER SERIALIZERS -------------------

class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields: list[str] = [
            "id",
            "question",
            "option",
            "correct",
            "comment_answer"
        ]
        depth = 2


class AnswerWriteSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Quiz.objects.all(),
        required=True,
        error_messages={
            "required": "A pergunta associada é obrigatória.",
            "does_not_exist": "Pergunta inválida.",
            "incorrect_type": "Pergunta inválida."
        }
    )
    option = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "A opção de resposta é obrigatória.",
            "blank": "A opção de resposta não pode ficar em branco."
        }
    )
    correct = serializers.BooleanField(
        required=True,
        error_messages={
            "required": "Defina se a resposta está correta."
        }
    )
    comment_answer = serializers.CharField(
        required=False,
        allow_blank=True
    )

    class Meta:
        model = Answer
        fields: list[str] = [
            "question",
            "option",
            "correct",
            "comment_answer"
        ]


# ------------------- SCORE SERIALIZERS -------------------

class ScoreDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True,
        error_messages={
            "required": "O usuário é obrigatório.",
            "does_not_exist": "Usuário inválido.",
            "incorrect_type": "Usuário inválido."
        }
    )
    answer_time = serializers.IntegerField(
        required=True,
        error_messages={
            "required": "O tempo de resposta é obrigatório.",
            "invalid": "Tempo de resposta inválido."
        }
    )
    type = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O tipo de quiz é obrigatório.",
            "blank": "O tipo de quiz não pode ficar em branco."
        }
    )
    level = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "required": "O nível do quiz é obrigatório.",
            "blank": "O nível do quiz não pode ficar em branco."
        }
    )
    system = serializers.PrimaryKeyRelatedField(
        queryset=System.objects.all(),  
        required=True,
        error_messages={
            "required": "O sistema relacionado é obrigatório.",
            "does_not_exist": "Sistema inválido.",
            "incorrect_type": "Sistema inválido."
        }
    )

    class Meta:
        model = Score
        fields: list[str] = [
            "id",
            "user",
            "answer_time",
            "type",
            "level",
            "system"
        ]
