"""
Django configuration for the Chat app.

This module contains the configuration for the 'chat' app, including the definition
of the AppConfig class for setting app name and auto field for primary keys.
"""

from django.apps import AppConfig


class ChatConfig(AppConfig):
    """
    Configuration for the Chat application.

    This class contains the settings and configuration for the 'chat' app in Django.
    It sets the default primary key field type and app name.
    """

    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'chat'
