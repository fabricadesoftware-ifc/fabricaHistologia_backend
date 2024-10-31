from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from uuid import uuid4
from core.user.models import PersonalData
from core.user.models import User
from tasks.contributor_send_email_verification import contributor_send_email_verification

@receiver(post_save, sender=PersonalData)
def contributor_verification(sender, instance, created, **kwargs):
    if created:
        user_personal_data = PersonalData.objects.get(id=instance.id).user
        user = User.objects.get(id=user_personal_data.id)

        print(user)

        token = str(uuid4())
        user.verification_token = token
        user.save()

        verify_url = reverse('verify-user', kwargs={'verification_token': token})
      

        id_user = user.id

        print("id_user: ", id_user)
        try: 
            print("Enviando email de verificação")
            contributor_send_email_verification.delay(id_user, verify_url)
        except Exception as e: 
            print("Erro ao enviar email de verificação:", str(e))


