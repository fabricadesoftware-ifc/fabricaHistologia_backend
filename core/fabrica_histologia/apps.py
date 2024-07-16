from django.apps import AppConfig


class FabricaHistologiaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.fabrica_histologia'

    def ready(self):
        import core.fabrica_histologia.signals