# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
# from django.urls import reverse
# from uuid import uuid4
# from core.usuario.models import Usuario

# @receiver(post_save, sender=Usuario)
# def send_verification_email(sender, instance, created, **kwargs):
#     if created:
#         # Gerar um token de verificação único
#         token = str(uuid4())
#         instance.verification_token = token
#         instance.save()

#         # Construir o link de verificação com o token
#         verify_url = reverse('verify-user', kwargs={'verification_token': token})
#         verify_link = f'http://localhost:5173/{verify_url}'

#         # Enviar email para conta administradora
#         admin_email = 'lucasantonete@hotmail.com'  
#         subject = 'Verificação de novo usuário'
#         message = f'Um novo usuário com o email:"{instance.email}" foi registrado. Para verificar, clique no link a seguir: {verify_link}'
#         send_mail(subject, message, settings.EMAIL_HOST_USER, [admin_email])