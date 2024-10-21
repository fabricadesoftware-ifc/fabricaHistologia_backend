from core.quiz.models import Answer, Quiz

from core.django_populate.infra.datas.answers import answers

def populate_answers():
    if Answer.objects.exists():
        return
    

    for answer_data in answers:
        try:
            quiz = Quiz.objects.get(id=answer_data["question_id"])
            
            # cria as respostas
            answer = Answer.objects.create(
                question=quiz,
                option=answer_data["option"],
                correct=answer_data["correct"],
                comment_answer=answer_data["comment_answer"]
            )

            answer.save()

        except Exception as e:
            print(f"Erro ao popular respostas '{answer_data['option']}': {e}")

    print("População de respostas concluídas.")