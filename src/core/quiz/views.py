from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from django_filters.rest_framework import DjangoFilterBackend

from core.quiz.models import Answer, Quiz, Score
from rest_framework.viewsets import ModelViewSet
from core.quiz.serializers import AnswerDetailSerializer, AnswerWriteSerializer, QuizDetailSerializer, QuizWriteSerializer, ScoreDetailSerializer
from core.quiz.filters import AnswerFilter, QuizFilter, ScoreFilter

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction


@extend_schema(tags=["Quiz"])
class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = QuizFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return QuizDetailSerializer
        return QuizWriteSerializer


@extend_schema(tags=["Answer"])
class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnswerFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return AnswerDetailSerializer
        return AnswerWriteSerializer

    @extend_schema(
        tags=["Answers"],
        description="Cria múltiplas respostas em uma única requisição"
    )
    @action(detail=False, methods=["post"], url_path="bulk-create")
    def bulk_create(self, request):
        """
        Cria múltiplas respostas em uma única requisição
        """
        serializer = AnswerWriteSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                serializer.save()
        except Exception as e:
            return Response(
                {"detail": f"Erro ao salvar respostas: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
@extend_schema(tags=["Score"])
class ScoreViewSet(ModelViewSet):
    queryset = Score.objects.all().order_by("answer_time")
    serializer_class = ScoreDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ScoreFilter
    
    