"""
Custom Django management command to start the RabbitMQ consumer.
"""

from typing import Any

from django.core.management.base import BaseCommand

from notifications.consumers import start_consumer


class Command(BaseCommand):
    help = "Starts the RabbitMQ consumer to handle customer events."

    def handle(self, *args: Any, **options: dict[str, Any]) -> None:
        self.stdout.write(self.style.SUCCESS("Launching consumer..."))
        try:
            start_consumer()
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Consumer interrupted. Shutting down."))
