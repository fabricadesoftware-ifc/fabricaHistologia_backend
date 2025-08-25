from django.db import models
from core.veterinary.models import System
from core.user.models import User

# Create your models here.

class Quiz(models.Model):
    title = models.TextField(null=True, max_length=155)
    question = models.TextField()
    system = models.ForeignKey(System, on_delete=models.PROTECT)

    levels = [
        (1, 'FACIL'),
        (2, 'MEDIO'),
        (3, 'DIFICIL')
    ]
    level = models.IntegerField(choices=levels)
    def __str__(self) -> str:
        return f"{self.question}"

class Answer(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    option = models.TextField()
    correct = models.BooleanField()
    comment_answer = models.TextField(blank=True, null=True, default="")

    def __str__(self) -> str:
        return f"{self.option}"
    
class Score(models.Model):
    type_choices = [
        (1, 'GERAL'),
        (2, 'SISTEMA')
    ]
    
    levels = [
        (1, 'FACIL'),
        (2, 'MEDIO'),
        (3, 'DIFICIL')
    ]
    
    
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="score_user")
    answer_time = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    type = models.IntegerField(choices=type_choices)
    level = models.IntegerField(choices=levels, null=True, blank=True)
    system = models.ForeignKey(System, on_delete=models.PROTECT, blank=True, null=True, related_name="score_system")
    
    def __str__(self):
        return f"{self.user} - {self.answer_time}"
        
    
    
    