import django_filters
from core.quiz.models import Answer, Quiz

class AnswerFilter(django_filters.FilterSet):
    question_id = django_filters.NumberFilter(field_name='question__id', lookup_expr='exact')
    level = django_filters.NumberFilter(field_name='level', lookup_expr='exact')
    
    class Meta:
        model = Answer
        fields = ['question_id']

class QuizFilter(django_filters.FilterSet):
    system_id = django_filters.NumberFilter(field_name='system__id', lookup_expr='exact')
    

    class Meta:
        model = Quiz
        fields = ['system_id', 'level']
    
