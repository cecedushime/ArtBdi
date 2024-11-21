from django.apps import AppConfig


class AppArtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_art'
class AppArtConfig(AppConfig):
    name = 'app_art'

    def ready(self):
        import app_art.signals