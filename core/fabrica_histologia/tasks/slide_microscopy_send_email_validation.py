from django.core.mail import send_mail
from django_project.settings import EMAIL_HOST_USER
from celery import shared_task
from core.fabrica_histologia.models import SlideMicroscopyPost

@shared_task
def slide_microscopy_send_email_validation(slide_post_id, verify_url):
    print('Sending email...')
    instance = SlideMicroscopyPost.objects.get(id=slide_post_id)

    verify_link = f'http://localhost:8000{verify_url}'

    email_user = instance.autor_user
    
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