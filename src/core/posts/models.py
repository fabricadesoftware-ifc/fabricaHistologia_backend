from django.db import models

from core.veterinary.models import Organ, Specie
from core.user.models import  User
from core.uploader.models import Image

class Posts(models.Model):
    class TypePost(models.IntegerChoices):
        HISTOLOGIA = 1, "Histologia"
        PATOLOGIA = 2, "Patologia"
    name = models.CharField(max_length=255)
    date_analysis = models.DateField()
    post_date = models.DateField()
    species = models.ForeignKey(Specie, on_delete=models.PROTECT)
    type_cut = models.CharField(max_length=255)
    increase = models.CharField(max_length=255)
    coloring = models.CharField(max_length=255)
    image = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    type_post = models.IntegerField(choices=TypePost.choices, default=TypePost.HISTOLOGIA)
    autor_user = models.ForeignKey(User, on_delete=models.PROTECT)
    organ = models.ForeignKey(Organ, on_delete=models.PROTECT)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    
    is_verified = models.BooleanField(default=False)  


    def __str__(self) -> str:
        return f"{self.name}"

    

class Point(models.Model):
    class ColorChoices(models.TextChoices):
        AMARELO = "yellow", 
        AZUL = "blue", 
        VERMELHO = "red",
    label_title = models.CharField(max_length=255)
    description = models.TextField()
    position = models.JSONField()
    color = models.CharField(choices=ColorChoices.choices, max_length=10)
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    analyzed_structures = models.CharField(max_length=255, null=True, blank=True)
    analyzed_functions = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.posts.name} - {self.label_title}"



    