from django.core.mail import send_mail
from django_project.settings import EMAIL_HOST_USER
from celery import shared_task
from core.usuario.models import Usuario

@shared_task
def contributor_send_email_verification(id_user, verify_url):

    instance = Usuario.objects.get(id=id_user)
    user_email = instance.email

    verify_link = f'http://localhost:8000{verify_url}'
    recipient_list = ['lucasantonete@hotmail.com']
    from_email = EMAIL_HOST_USER

    send_mail(
        'Verificação de novo usuário',
        f'Um novo usuário com o email:"{user_email}" foi registrado. Para verificar, clique no link a seguir: {verify_link}',
        recipient_list=recipient_list,
        from_email=from_email
    )
