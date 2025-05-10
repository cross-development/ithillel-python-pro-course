import json
import time

import pika
from pika.spec import Basic
from pika.adapters.blocking_connection import BlockingChannel
from django.conf import settings


def callback(ch: BlockingChannel, method: Basic.Deliver, properties: pika.BasicProperties, body: bytes) -> None:
    """
    Callback function that handles the messages from RabbitMQ.

    Args:
        ch (BlockingChannel): The channel that received the message.
        method (Basic.Deliver): The delivery method details.
        properties (pika.BasicProperties): The message properties.
        body (bytes): The message body as a byte string.

    Returns:
        None: This function doesn't return anything but acknowledges the message.
    """

    event = method.routing_key
    data = json.loads(body)
    # Simulate sending email by printing
    print(f"[EMAIL] Event: {event}, payload: {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_consumer() -> None:
    """
    Starts the RabbitMQ consumer to handle customer events.

    This function connects to RabbitMQ, sets up the exchange and queues,
    and listens for incoming messages on the 'customer.created' and
    'customer.updated' routing keys.

    Returns:
        None: This function doesn't return anything.
    """

    while True:
        try:
            creds = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASS)
            conn = pika.BlockingConnection(
                pika.ConnectionParameters(host=settings.RABBITMQ_HOST, credentials=creds)
            )
            break
        except pika.exceptions.AMQPConnectionError:
            print("Cannot connect to RabbitMQ, retrying in 2 seconds...")
            time.sleep(2)

    channel = conn.channel()
    channel.exchange_declare(exchange="customer_events", exchange_type="topic", durable=True)
    q = channel.queue_declare("", exclusive=True)
    queue_name = q.method.queue

    channel.queue_bind(exchange="customer_events", queue=queue_name, routing_key="customer.created")
    channel.queue_bind(exchange="customer_events", queue=queue_name, routing_key="customer.updated")

    print(" [*] Waiting for customer events. To exit press CTRL+C")
    channel.basic_consume(queue=queue_name, on_message_callback=callback)
    channel.start_consuming()
