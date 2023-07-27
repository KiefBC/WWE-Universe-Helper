from django.apps import AppConfig
from django.core.cache import cache
from django.core.management import call_command
from django.db import connection


class WweuniversewebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WWEUniverseWebApp'

    # This is where we import our signals
    def ready(self):
        """
        This method is called when our app is ready.
        """
        # Import our signals
        import WWEUniverseWebApp.signals

        if not cache.get('db_reset_run'):
            with connection.cursor() as cursor:
                # Check if we have any tables
                table_count = cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table';").fetchall()
                # If we have tables, drop them
                if len(table_count) > 0:
                    # If we need to reset our database, call our reset_db command
                    call_command('reset_db')
                    # Set our cache to True
                    cache.set('db_reset_run', True)
