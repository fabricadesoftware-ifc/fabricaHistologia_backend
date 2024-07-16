from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from asgiref.sync import async_to_sync
from uuid import uuid4
from core.fabrica_histologia.use_case.slide_microscopy_send_email_validation import slide_microscopy_send_email_validation
from core.fabrica_histologia.models import SlideMicroscopyPost

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