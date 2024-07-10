from django.db import models
from core.fabrica_histologia.models import System

# Create your models here.

class Quiz(models.Model):
    question = models.TextField()
    level = models.CharField(max_length=255)
    system = models.ForeignKey(System, on_delete=models.PROTECT)

class Answer(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    option = models.TextField()
    correct = models.BooleanField()
    comment_answer = models.TextField(default="")
    


