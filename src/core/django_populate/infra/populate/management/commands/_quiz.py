from core.quiz.models import Quiz
from core.veterinary.models import System

from core.django_populate.infra.datas.quiz import quizzes

def populate_quizzes():
    if Quiz.objects.exists():
        return
    

    for quiz_data in quizzes:
        try:
            system = System.objects.get(id=quiz_data["system_id"])
            
            # cria os sistemas
            quiz = Quiz.objects.create(
                question=quiz_data["question"],
                level=quiz_data["level"],
                system=system
            )

            quiz.save()

        except Exception as e:
            print(f"Erro ao popular quizzes '{quiz_data['question']}': {e}")

    print("População de quizzes concluídas.")