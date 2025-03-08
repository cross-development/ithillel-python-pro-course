"""
App configuration for the Home application.

This module defines the configuration settings for the Home app.
"""

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration class for the Home app.

    Attributes:
        default_auto_field (str): Specifies the default type for auto-incrementing primary keys.
        name (str): The name of the application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
