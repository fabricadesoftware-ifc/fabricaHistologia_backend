import os

from django.core.mail import send_mail
from celery import shared_task

from django_project.settings import EMAIL_HOST_USER
from core.user.models import User

@shared_task
def recover_password_code(user_id, code):

    user = User.objects.get(id=user_id)
    recipient_list: list[str] = [user.email]
    from_email: str = EMAIL_HOST_USER
    message: str = f"Seu código de recuperação de senha é: {code}"

    send_mail(
        subject='Recuperação de senha',
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
)
