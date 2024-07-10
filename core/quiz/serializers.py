from core.quiz.models import Quiz, Answer
from rest_framework.serializers import ModelSerializer

class QuizDetailSerializer(ModelSerializer):
    class Meta: 
        model = Quiz
        fields: list[str] = [
            "id",
            "question",
            "level",
            "system"
        ]

class QuizWriteSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields: list[str] = [
            "question",
            "level",
            "system"
        ]

class AnswerDetailSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields: list[str] = [
            "id",
            "question",
            "option",
            "correct",
            "comment_answer"
        ]

class AnswerWriteSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields: list[str] = [
            "question",
            "option",
            "correct",
            "comment_answer"
        ]