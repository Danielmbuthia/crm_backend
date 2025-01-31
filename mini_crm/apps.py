from django.apps import AppConfig


class MiniCrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mini_crm'

    def ready(self):
        import mini_crm.signals
