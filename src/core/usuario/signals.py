from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from uuid import uuid4
from core.usuario.models import Usuario
from core.usuario.tasks.contributor_send_email_verification import contributor_send_email_verification

@receiver(post_save, sender=Usuario)
def contributor_verification(sender, instance, created, **kwargs):
    """
    Signal handler function that is triggered after a new 'Usuario' instance is saved.
    It generates a verification token, saves it to the instance, and sends an email with a verification link.

    Args:
        sender: The sender of the signal.
        instance: The 'Usuario' instance that was saved.
        created: A boolean indicating if the instance was newly created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        token = str(uuid4())
        instance.verification_token = token
        instance.save()

        verify_url = reverse('verify-user', kwargs={'verification_token': token})
      

        id_user = instance.id

        print("id_user: ", id_user)
        try: 
            print("Enviando email de verificação")
            contributor_send_email_verification.delay(id_user, verify_url)
        except: 
            print("Erro ao enviar email de verificação")


