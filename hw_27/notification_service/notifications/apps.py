"""
Django app configuration for the Notifications app.
"""

from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notifications"

    def ready(self) -> None:
        """
        Override the ready method to configure app-specific tasks.

        In this case, no automatic thread is started as the consumer
        is launched via the management command.
        """

        pass
