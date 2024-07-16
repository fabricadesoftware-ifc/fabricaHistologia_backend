import asyncio
from django.core.mail import send_mail
from django_project.settings import EMAIL_HOST_USER
from django.urls import reverse


async def slide_microscopy_send_email_validation(instance, verify_url, email_user):
    await asyncio.sleep(1)
    
    verify_link = f'http://localhost:8000{verify_url}'

    email_user = email_user
    recipient_list = ['lucasantonete@hotmail.com']
    subject = 'Verificação de nova postagem no projeto de histologia'
    message = (
        f'Uma nova postagem foi realizada por um colaborador. Para verificar, clique no link a seguir: {verify_link}\n\n'
        f'O colaborador responsável pela postagem é: {email_user}'
    )
    from_email = EMAIL_HOST_USER

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )