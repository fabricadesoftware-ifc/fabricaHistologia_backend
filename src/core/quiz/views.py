from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from django_filters.rest_framework import DjangoFilterBackend

from core.quiz.models import Answer, Quiz
from rest_framework.viewsets import ModelViewSet
from core.quiz.serializers import AnswerDetailSerializer, AnswerWriteSerializer, QuizDetailSerializer, QuizWriteSerializer
from core.quiz.filters import AnswerFilter, QuizFilter



@extend_schema(tags=["Quiz"])
class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = QuizFilter
    
    def get_serializer_class(self):
        if self.action in ["list"]:            
            return QuizDetailSerializer
        elif self.action in ["retrieve"]:
            return QuizDetailSerializer
        return QuizWriteSerializer


@extend_schema(tags=["Answer"])
class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnswerFilter
    
    def get_serializer_class(self):
        if self.action in ["list"]:            
            return AnswerDetailSerializer
        elif self.action in ["retrieve"]:
            return AnswerDetailSerializer
        return AnswerWriteSerializer
    