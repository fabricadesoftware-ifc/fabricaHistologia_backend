from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from uuid import uuid4
from core.fabrica_histologia.tasks.slide_microscopy_send_email_validation import slide_microscopy_send_email_validation
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

        token = str(uuid4())
        instance.verification_token = token
        instance.save()

        slide_post_id = instance.id

        verify_url = reverse('verify-post', kwargs={'verification_token': token})


        slide_microscopy_send_email_validation.delay(slide_post_id, verify_url)