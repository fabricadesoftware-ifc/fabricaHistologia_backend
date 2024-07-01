from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from uuid import uuid4
from core.usuario.models import Usuario
from django_project.settings import EMAIL_HOST_USER

@receiver(post_save, sender=Usuario)
def send_verification_email(sender, instance, created, **kwargs):
    if created:
        # Gerar um token de verificação único
        token = str(uuid4())
        instance.verification_token = token
        instance.save()

        # Construir o link de verificação com o token
        verify_url = reverse('verify-user', kwargs={'verification_token': token})
        print("verify_url: ", verify_url)
        verify_link = f'http://localhost:8000/{verify_url}'

        print(EMAIL_HOST_USER)
        # Enviar email para conta administradora
        recipient_list = ['lucasantonete@hotmail.com']  
        subject = 'Verificação de novo usuário'
        from_email = "fabricahistologia@gmail.com"
        print("EMAIL")
        message = f'Um novo usuário com o email:"{instance.email}" foi registrado. Para verificar, clique no link a seguir: {verify_link}'
        print("MESSAGE", message)
        try:    
            send_mail(
                subject, 
                message, 
                recipient_list = recipient_list, 
                from_email = from_email
                ) 
        except Exception as e:
            print("nao foi porra nenhuma")