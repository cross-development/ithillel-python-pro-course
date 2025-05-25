"""
Signal handlers for the Customer model.

Publishes a message to RabbitMQ when a customer is created or updated.
"""

import json
from typing import Any

import pika
from django.conf import settings
from django.db.models import Model
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Customer


@receiver(post_save, sender=Customer)
def publish_customer_event(sender: type[Model], instance: Customer, created: bool, **kwargs: Any) -> None:
    """
    Publishes a customer event message to a RabbitMQ exchange
    when a Customer instance is created or updated.

    Args:
        sender (type[Model]): The model class.
        instance (Customer): The actual instance being saved.
        created (bool): True if a new record was created.
        **kwargs (Any): Additional keyword arguments.
    """

    routing_key: str = 'customer.created' if created else 'customer.updated'
    message: dict[str, Any] = {
        'id': instance.id,
        'email': instance.email,
        'first_name': instance.first_name,
        'last_name': instance.last_name,
        'timestamp': instance.updated_at.isoformat(),
    }

    credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASS)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ_HOST, credentials=credentials)
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='customer_events', exchange_type='topic', durable=True)
    channel.basic_publish(
        exchange='customer_events',
        routing_key=routing_key,
        body=json.dumps(message),
        properties=pika.BasicProperties(content_type='application/json')
    )
    connection.close()
