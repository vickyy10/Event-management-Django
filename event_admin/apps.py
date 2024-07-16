from django.apps import AppConfig


class EventAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'event_admin'

    def ready(self):
        import event_admin.signals 
