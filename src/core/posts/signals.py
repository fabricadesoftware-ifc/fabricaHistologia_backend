from django.db.models.signals import post_save
from django.dispatch import receiver


from django_project.settings import EMAIL_RECEIVER_HISTOLOGY_USER, EMAIL_RECEIVER_PATHOLOGY_USER
from tasks.post_validation import post_validation
from core.posts.models import Posts
from core.user.models import User

@receiver(post_save, sender=Posts)
def post_signal_validation(sender, instance, created, **kwargs ):
    if created:
        post = Posts.objects.get(id=instance.id)
        user_email = post.autor_user
        user_id = User.objects.get(email=user_email).id
       
        print(user_id)
        post_type = post.type_post
        slide_post_id = instance.id
        
        if post_type == 1:
            EMAIL_RECEIVER_USER = EMAIL_RECEIVER_HISTOLOGY_USER
        elif post_type == 2:
            EMAIL_RECEIVER_USER = EMAIL_RECEIVER_PATHOLOGY_USER

        post_validation.delay(slide_post_id,  EMAIL_RECEIVER_USER, user_id)