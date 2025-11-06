from django.shortcuts import render
from drf_spectacular.utils import extend_schema

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F
from core.quiz.models import Answer, Quiz, Score
from rest_framework.viewsets import ModelViewSet
from core.quiz.serializers import AnswerDetailSerializer, AnswerWriteSerializer, QuizDetailSerializer, QuizWriteSerializer, ScoreDetailSerializer
from core.quiz.filters import AnswerFilter, QuizFilter, ScoreFilter
from rest_framework import status, viewsets
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


@extend_schema(tags=["Top Scores"])
class TopScoresViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ScoreDetailSerializer
    queryset = Score.objects.all().select_related("user")  # 🔹 otimiza as queries

    @action(detail=False, methods=["get"])
    def ranking(self, request):
        type_ = request.query_params.get("type")
        level = request.query_params.get("level")
        user = request.user

        # 🔹 Base query
        queryset = self.queryset

        # 🔹 Filtro condicional
        if type_:
            queryset = queryset.filter(type=type_)

            # Se for "geral" (type=1), aplica level
            if str(type_) == "1" and level:
                queryset = queryset.filter(level=level)
            # Se for "específico" (type=2), ignora level
            elif str(type_) == "2":
                queryset = queryset.filter(level__isnull=True)

        # 🔹 Ordenação: score desc / tempo asc
        queryset = queryset.order_by("-score", "answer_time")

        # 🔹 Top 10
        top_10 = queryset[:10]

        # 🔹 Serialização mínima (eficiente)
        results = [
            {
                "pos": idx + 1,
                "email": s.user.email if s.user else "Desconhecido",
                "score": s.score or 0,
                "answer_time": float(s.answer_time or 0),
            }
            for idx, s in enumerate(top_10)
        ]

        # 🔹 Dados do usuário logado
        user_score_data = None
        user_position = None

        if user.is_authenticated:
            all_scores = list(queryset)
            for idx, score in enumerate(all_scores, 1):
                if score.user_id == user.id:
                    user_position = idx
                    user_score_data = {
                        "pos": idx,
                        "email": score.user.email,
                        "score": score.score or 0,
                        "answer_time": float(score.answer_time or 0),
                    }
                    break

        # 🔹 Retorno final
        return Response(
            {
                "results": results,
                "user_score": user_position,
                "user_score_data": user_score_data,
            },
            status=status.HTTP_200_OK,
        )
