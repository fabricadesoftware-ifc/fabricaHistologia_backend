from django.apps import AppConfig


class UsuarioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.usuario"

    def ready(self):
        import core.usuario.signals