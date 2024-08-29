from django.db import models
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

    def __str__(self) -> str:
        return f"{self.name}"
    
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

    def __str__(self) -> str:
        return f"{self.name}"

class Specie(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"



