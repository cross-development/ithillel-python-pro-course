"""
App configuration for the main application.

This module defines the configuration settings for the main app.
"""

from django.apps import AppConfig


class MainConfig(AppConfig):
    """
    Configuration class for the main app.

    Attributes:
        default_auto_field (str): Specifies the default type for auto-incrementing primary keys.
        name (str): The name of the application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
