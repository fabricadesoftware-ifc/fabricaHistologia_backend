from django.db import models
from core.usuario.models import Usuario as User
from core.uploader.models import Image

class System(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_system = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

class Organ(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_organ = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    system = models.ForeignKey(System, on_delete=models.PROTECT)

class Specie(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

class SlideMicroscopyPost(models.Model):
    date_analysis = models.DateField()
    post_date = models.DateField()
    species = models.ForeignKey(Specie, on_delete=models.PROTECT)
    type_cut = models.CharField(max_length=255)
    increase = models.CharField(max_length=255)
    coloring = models.CharField(max_length=255)
    image_slide = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    autor_user = models.ForeignKey(User, on_delete=models.PROTECT)
    organ = models.ForeignKey(Organ, on_delete=models.PROTECT)

class Point(models.Model):
    label_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    position = models.JSONField()
    color = models.CharField(max_length=255)
    slide = models.ForeignKey(SlideMicroscopyPost, on_delete=models.PROTECT)
    analyzed_structures = models.CharField(max_length=255)
    analyzed_functions = models.CharField(max_length=255)



    

