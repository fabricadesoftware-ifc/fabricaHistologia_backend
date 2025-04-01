import os

from django.utils.html import strip_tags
from django.core.mail import send_mail
from celery import shared_task

from django_project.settings import EMAIL_HOST_USER, EMAIL_RECEIVER_HISTOLOGY_USER, EMAIL_RECEIVER_PATHOLOGY_USER, BASE_DIR
from core.user.models import User, PersonalData
from django_project.settings import API_URL

@shared_task
def contributor_send_email_verification(id_user, verify_url):

    instance: User = User.objects.get(id=id_user)
    personal_data: PersonalData = PersonalData.objects.get(user=instance)
    user_email: str = instance.email
    birth_date: str = personal_data.birth_date.strftime("%Y-%m-%d")

    verify_link: str = f"{API_URL}/{verify_url}"
    recipient_list: list[str] = [EMAIL_RECEIVER_HISTOLOGY_USER, EMAIL_RECEIVER_PATHOLOGY_USER]
    from_email: str = EMAIL_HOST_USER

    with open(os.path.join(BASE_DIR, 'templates/contribuitor_email_template.html'), 'r') as file:
            html = file.read()
            html = html.replace('personal_data.name', personal_data.name)
            html = html.replace('user_email', user_email)
            html = html.replace('personal_data.registration', personal_data.registration)
            html = html.replace('personal_data.birth_date', birth_date)
            html = html.replace('personal_data.phone', personal_data.phone)
            html = html.replace('personal_data.education_level', personal_data.education_level)
            html = html.replace('personal_data.university', personal_data.university)
            html = html.replace('verify_link', verify_link)
                     

    print(html)

    plain_message = strip_tags(html)

    send_mail(
        subject='Verificação de novo usuário',
        message=plain_message,
        html_message=html,
        from_email=from_email,
        recipient_list=recipient_list,
)
