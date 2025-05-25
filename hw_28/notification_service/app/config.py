from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    Attributes:
        RABBITMQ_HOST (str): Hostname or IP of the RabbitMQ server.
        RABBITMQ_USER (str): Username for RabbitMQ authentication.
        RABBITMQ_PASS (str): Password for RabbitMQ authentication.
        EXCHANGE_NAME (str): Name of the RabbitMQ exchange.
        EXCHANGE_TYPE (str): Type of the RabbitMQ exchange.
        ROUTING_KEYS (list[str]): List of routing keys to bind.
        DEFAULT_FROM_EMAIL (str): Default sender email address.
    """

    RABBITMQ_HOST: str
    RABBITMQ_USER: str
    RABBITMQ_PASS: str
    EXCHANGE_NAME: str = "customer_events"
    EXCHANGE_TYPE: str = "topic"
    ROUTING_KEYS: list[str] = ["customer.created", "customer.updated"]
    DEFAULT_FROM_EMAIL: str = "noreply@booklibrary.com"

    class Config:
        """
        Pydantic configuration for environment file.
        """

        env_file = ".env"
        env_file_encoding = 'utf-8'
