from django.core.mail import send_mail
from celery import shared_task

from django_project.settings import EMAIL_HOST_USER, EMAIL_RECEIVER_HISTOLOGY_USER, EMAIL_RECEIVER_PATHOLOGY_USER
from core.user.models import User, PersonalData
from django_project.settings import API_URL

@shared_task
def contributor_send_email_verification(id_user, verify_url):

    instance: User = User.objects.get(id=id_user)
    personal_data: PersonalData = PersonalData.objects.get(user=instance)
    user_email: str = instance.email

    verify_link: str = f"{API_URL}/{verify_url}"
    recipient_list: list[str] = [EMAIL_RECEIVER_HISTOLOGY_USER, EMAIL_RECEIVER_PATHOLOGY_USER]
    from_email: str = EMAIL_HOST_USER

    send_mail(
    'Verificação de novo usuário',
    f'Um novo usuário requer verificação.\n'
    f'Nome: {personal_data.name},\n'
    f'Email: {user_email},\n'
    f'Registro: {personal_data.registration},\n'
    f'Data de nascimento: {personal_data.birth_date},\n'
    f'Telefone: {personal_data.phone},\n'
    f'Nível de escolaridade: {personal_data.education_level},\n'
    f'Universidade: {personal_data.university}\n'
    f'Por favor, clique no link para verificar o usuário: {verify_link}',
    recipient_list=recipient_list,
    from_email=from_email
)
