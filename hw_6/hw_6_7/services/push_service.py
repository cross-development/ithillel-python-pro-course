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
