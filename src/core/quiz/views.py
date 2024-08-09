from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from core.quiz.models import Answer, Quiz
from rest_framework.viewsets import ModelViewSet
from core.quiz.serializers import AnswerDetailSerializer, AnswerWriteSerializer, QuizDetailSerializer, QuizWriteSerializer

@extend_schema(tags=["Quiz"])
class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list"]:            
            return QuizDetailSerializer
        elif self.action in ["retrieve"]:
            return QuizDetailSerializer
        return QuizWriteSerializer


@extend_schema(tags=["Answer"])
class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list"]:            
            return AnswerDetailSerializer
        elif self.action in ["retrieve"]:
            return AnswerDetailSerializer
        return AnswerWriteSerializer
    