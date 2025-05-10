"""
App configuration for the customers app.

Includes automatic import of signal handlers when the app is ready.
"""

from django.apps import AppConfig


class CustomersConfig(AppConfig):
    """
    Configuration class for the customers Django app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'

    def ready(self):
        import customers.signals
