from rest_framework.routers import DefaultRouter

from core.quiz.views import AnswerViewSet, QuizViewSet, ScoreViewSet

router = DefaultRouter()

router.register(r"quiz", QuizViewSet)
router.register(r"answer", AnswerViewSet)
router.register(r"score", ScoreViewSet)


