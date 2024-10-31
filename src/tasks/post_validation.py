from django.core.mail import send_mail
from django_project.settings import EMAIL_HOST_USER
from celery import shared_task
from core.posts.models import Posts
from core.user.models import User, PersonalData
from django.urls import reverse
from uuid import uuid4
from django_project.settings import API_URL


@shared_task
def post_validation(slide_post_id, EMAIL_RECEIVER_USER, user_id):
    print('Sending email...')
    instance: Posts = Posts.objects.get(id=slide_post_id)
    user: User = User.objects.get(id=user_id)
    personal_data: PersonalData = PersonalData.objects.get(user=user)

    token = str(uuid4())
    instance.verification_token = token
    instance.save()

   
    verify_url = reverse('verify-post', kwargs={'verification_token': token})

    verify_link = f'{API_URL}/{verify_url}'

    email_user: str = instance.autor_user
    from_email: str = EMAIL_HOST_USER

    recipient_list: list[str] = [EMAIL_RECEIVER_USER]
    subject: str = 'Verificação de nova postagem'
    message = (
        f'Uma nova postagem foi realizada por um colaborador. '
        f'Para verificar, clique no link a seguir: {verify_link}\n'
        f'O colaborador responsável pela postagem é: {email_user}'
        f'Nome: {personal_data.name}\n'
        f'Registro: {personal_data.registration}\n'
        f"Universidade: {personal_data.university}\n"
        f"Escolaridade: {personal_data.education_level}\n"
        f"Data de Nascimento: {personal_data.birth_date}\n"
    )

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )