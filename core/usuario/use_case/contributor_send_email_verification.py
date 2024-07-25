import asyncio
from django.core.mail import send_mail
from django_project.settings import EMAIL_HOST_USER


async def contributor_send_email_verification(instance, verify_link):
    await asyncio.sleep(1)

    recipient_list = ['lucasantonete@hotmail.com']
    from_email = EMAIL_HOST_USER

    send_mail(
        'Verificação de novo usuário',
        f'Um novo usuário com o email:"{instance.email}" foi registrado. Para verificar, clique no link a seguir: {verify_link}',
        recipient_list=recipient_list,
        from_email=from_email
    )
