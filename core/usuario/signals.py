from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from asgiref.sync import async_to_sync
from uuid import uuid4
from core.usuario.models import Usuario
from core.usuario.use_case.contributor_send_email_verification import contributor_send_email_verification
from core.usuario.use_case.slide_microscopy_send_email_validation import slide_microscopy_send_email_validation
from core.fabrica_histologia.models import SlideMicroscopyPost

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
        print("verify_url: ", verify_url)
        verify_link = f'http://localhost:8000/{verify_url}'

        async_to_sync(contributor_send_email_verification)(instance, verify_link)


@receiver(post_save, sender=SlideMicroscopyPost)
def slide_microscopy_post_verification(sender, instance, created, **kwargs ):
    """
    Signal handler for verifying a SlideMicroscopyPost instance.

    This function is triggered after a SlideMicroscopyPost instance is saved.
    It generates a verification token, saves it to the instance, and sends an email
    to the author user with a verification URL.

    Parameters:
    - sender: The sender of the signal (SlideMicroscopyPost).
    - instance: The instance of SlideMicroscopyPost being saved.
    - created: A boolean indicating if the instance was created or updated.
    - kwargs: Additional keyword arguments.
    """
    if created:
        email_user = instance.autor_user
        
        token = str(uuid4())
        instance.verification_token = token
        instance.save()

        verify_url = reverse('verify-post', kwargs={'verification_token': token})

        async_to_sync(slide_microscopy_send_email_validation)(instance, verify_url, email_user)