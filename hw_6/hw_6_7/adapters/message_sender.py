"""
This module defines the MessageSender abstract base class.

The MessageSender interface defines a common method, `send_message(message)`,
for sending messages through various channels (e.g., email, SMS, push notifications).

Subclasses of MessageSender are expected to implement this method
with the specific logic for sending messages via their respective channels.

This interface promotes consistent message sending behavior
across different communication channels.
"""


class MessageSender:
    """
    Base class for message senders.

    Subclasses should implement the `send_message` method to send messages
    using their specific channels (e.g., email, SMS, push notifications).
    """

    def send_message(self, message: str) -> None:
        """
        Sends a message.

        This method is to be implemented by subclasses.

        Args:
            message (str): The message to send.
        """
