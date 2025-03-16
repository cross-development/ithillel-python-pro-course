"""
App configuration for the application.

This module defines the configuration settings for the app.
"""

from django.apps import AppConfig


class BoardConfig(AppConfig):
    """
    Configuration class for the app.

    Attributes:
        default_auto_field (str): Specifies the default type for auto-incrementing primary keys.
        name (str): The name of the application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'

    def ready(self) -> None:
        """
        Import signals when the app is ready.
        """

        import board.signals  # Register signals
