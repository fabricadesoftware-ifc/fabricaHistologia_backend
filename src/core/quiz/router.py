from rest_framework.routers import DefaultRouter

from core.quiz.views import AnswerViewSet, QuizViewSet, ScoreViewSet, TopScoresView

router = DefaultRouter()

router.register(r"quiz", QuizViewSet)
router.register(r"answer", AnswerViewSet)
router.register(r"score", ScoreViewSet)
router.register(r"top-scores", TopScoresView, basename="top-scores")


