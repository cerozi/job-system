from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.notifications'

    def ready(self) -> None:
        # import signals;
        import apps.notifications.signals
        return super().ready()
