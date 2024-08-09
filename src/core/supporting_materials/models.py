from django.db import models
from core.uploader.models import Image, Document
from core.fabrica_histologia.models import System
# Create your models here.

class SupportingMaterial(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_supporting_material = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    document_supporting_material = models.ForeignKey(
        Document,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    field_name = models.URLField(max_length=200)
    system = models.ForeignKey(System, on_delete=models.PROTECT)