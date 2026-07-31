from django.apps import AppConfig


class InteractionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'interactions'
    verbose_name= 'Interactions'

    def ready(self):
        import interactions.signals