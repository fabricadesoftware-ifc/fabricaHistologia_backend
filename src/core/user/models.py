from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    passage_id = models.CharField(max_length=255, unique=True)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]


class PersonalData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    registration = models.CharField(max_length=20)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    class education_level(models.TextChoices):
        MEDIO = "Médio", _("Médio")
        SUPERIOR = "Superior", _("Superior")
        POS_GRADUACAO = "Pós-Graduação", _("Pós-Graduação")
        MESTRADO = "Mestrado", _("Mestrado")
        DOUTORADO = "Doutorado", _("Doutorado")
        POS_DOUTORADO = "Pós-Doutorado", _("Pós-Doutorado")
    education_level = models.CharField(
        max_length=20,
        choices=education_level.choices,
        default=education_level.MEDIO,
    )
    university = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dados Pessoais"
        verbose_name_plural = "Dados Pessoais"
        ordering = ["name"]