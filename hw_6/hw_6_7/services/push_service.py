"""
This module defines the PushService class, which simulates the functionality
of a push notification service.

The PushService provides a `send_push` method that:

- Takes the device ID and the push notification message as input.
- Performs basic validation of the device ID format.
- Simulates sending the push notification by printing a confirmation message.

This class can be used as a placeholder or for testing purposes
before integrating with a real push notification service.
"""


class PushService:
    """
    Class representing a push notification service.
    """

    def send_push(self, device_id: str, message: str) -> None:
        """
        Sends a push notification.

        Args:
            device_id (str): The ID of the target device.
            message (str): The push notification message.

        Raises:
            ValueError: If the device ID format is invalid.
        """

        if not device_id.startswith("device"):
            raise ValueError("Invalid device ID format")

        print(f"Push notification sent to device {device_id}: {message}")
