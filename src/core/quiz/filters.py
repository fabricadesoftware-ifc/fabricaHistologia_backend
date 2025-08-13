import django_filters
from core.quiz.models import Answer, Quiz, Score

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
        
class ScoreFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(field_name='user__id', lookup_expr='exact')
    type = django_filters.NumberFilter(field_name='type', lookup_expr='exact')
    level = django_filters.NumberFilter(field_name='level', lookup_expr='exact')
    system_id = django_filters.NumberFilter(field_name='system__id', lookup_expr='exact')

    class Meta:
        model = Score
        fields = ['user_id', 'type', 'level', 'system_id']

    
