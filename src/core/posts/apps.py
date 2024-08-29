from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.posts'
    
    def ready(self):
        import core.posts.signals
