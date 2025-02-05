"""
This module defines the PushAdapter class, which adapts the PushService
interface to the MessageSender interface.

The PushAdapter:

- Uses the PushService to send push notifications.
- Encapsulates the device ID for targeted push notifications.
- Provides a consistent `send_message` interface that aligns with the MessageSender.

This adapter facilitates the use of the PushService within a system
that expects a more generic MessageSender interface.
"""

from hw_6.hw_6_7.adapters.message_sender import MessageSender
from hw_6.hw_6_7.services.push_service import PushService


class PushAdapter(MessageSender):
    """
    Adapter class to send messages via push service.
    """

    def __init__(self, push_service: PushService, device_id: str) -> None:
        """
        Initializes the PushAdapter.

        Args:
            push_service (PushService): A push service instance.
            device_id (str): The device ID to send push notifications to.
        """

        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str) -> None:
        """
        Sends a message via push notification.

        Args:
            message (str): The message to send.

        Raises:
            Exception: For any errors during sending push notification.
        """

        try:
            self.push_service.send_push(self.device_id, message)
        except Exception as e:
            print(f"Error sending push-message: {e}")
