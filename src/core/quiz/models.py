from django.db import models
from core.veterinary.models import System

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
    comment_answer = models.TextField(default="")

    def __str__(self) -> str:
        return f"{self.option}"
    


