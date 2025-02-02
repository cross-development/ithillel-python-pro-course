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
