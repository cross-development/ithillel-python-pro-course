import json
import time
import threading
import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic

from .config import Settings


def callback(
        ch: BlockingChannel,
        method: Basic.Deliver,
        properties: pika.BasicProperties,
        body: bytes
) -> None:
    """
    Handle incoming RabbitMQ messages and acknowledge them.

    Args:
        ch (BlockingChannel): Channel that received the message.
        method (Basic.Deliver): Delivery method information.
        properties (pika.BasicProperties): Message properties.
        body (bytes): Raw message body.
    """

    event = method.routing_key
    data = json.loads(body)
    # Simulate sending email by printing to console
    print(f"[EMAIL] Event: {event}, payload: {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_consumer() -> None:
    """
    Connect to RabbitMQ and start consuming messages.

    This function will retry connecting on failure and bind to configured routing keys.
    """

    settings = Settings()

    # Retry loop until connection is established
    while True:
        try:
            credentials = pika.PlainCredentials(
                settings.RABBITMQ_USER, settings.RABBITMQ_PASS
            )
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=settings.RABBITMQ_HOST,
                    credentials=credentials
                )
            )
            break
        except pika.exceptions.AMQPConnectionError:
            print("Cannot connect to RabbitMQ, retrying in 2 seconds...")
            time.sleep(2)

    channel = connection.channel()
    channel.exchange_declare(
        exchange=settings.EXCHANGE_NAME,
        exchange_type=settings.EXCHANGE_TYPE,
        durable=True
    )

    queue = channel.queue_declare(queue="", exclusive=True)
    queue_name: str = queue.method.queue

    for rk in settings.ROUTING_KEYS:
        channel.queue_bind(
            exchange=settings.EXCHANGE_NAME,
            queue=queue_name,
            routing_key=rk
        )

    print("[*] Waiting for customer events. To exit press CTRL+C")
    channel.basic_consume(queue=queue_name, on_message_callback=callback)
    channel.start_consuming()


def run_consumer_in_thread() -> None:
    """
    Launch the RabbitMQ consumer in a background daemon thread.
    """

    thread = threading.Thread(target=start_consumer, daemon=True)
    thread.start()
