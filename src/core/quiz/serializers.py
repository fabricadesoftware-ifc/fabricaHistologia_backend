from core.quiz.models import Quiz, Answer, Score
from rest_framework.serializers import ModelSerializer

class QuizDetailSerializer(ModelSerializer):
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

class QuizWriteSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields: list[str] = [
            "title",
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
        depth = 2

class AnswerWriteSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields: list[str] = [
            "id",
            "question",
            "option",
            "correct",
            "comment_answer"
        ]
    
        
class ScoreDetailSerializer(ModelSerializer):
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