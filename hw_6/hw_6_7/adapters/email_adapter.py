"""
This module defines the EmailAdapter class, which adapts the EmailService
interface to the MessageSender interface.

The EmailAdapter:

- Uses the EmailService to send email messages.
- Encapsulates the email address from which messages are sent.
- Provides a consistent `send_message` interface that aligns with the MessageSender.

This adapter facilitates the use of the EmailService within a system
that expects a more generic MessageSender interface.
"""

from hw_6.hw_6_7.adapters.message_sender import MessageSender
from hw_6.hw_6_7.services.email_service import EmailService


class EmailAdapter(MessageSender):
    """
    Adapter class to send messages via email service.
    """

    def __init__(self, email_service: EmailService, email_address: str) -> None:
        """
        Initializes the EmailAdapter.

        Args:
            email_service (EmailService): An email service instance.
            email_address (str): The email address to send messages from.
        """

        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str) -> None:
        """
        Sends a message via email.

        Args:
            message (str): The message to send.

        Raises:
            Exception: For any errors during sending email.
        """

        try:
            self.email_service.send_email(self.email_address, message)
        except Exception as e:
            print(f"Error sending email: {e}")
