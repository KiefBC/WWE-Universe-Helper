from django.apps import AppConfig


class WweuniversewebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WWEUniverseWebApp'

    # This is where we import our signals
    def ready(self):
        import WWEUniverseWebApp.signals