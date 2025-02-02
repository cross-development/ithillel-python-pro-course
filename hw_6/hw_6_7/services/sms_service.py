class SmsService:
    """
    Class representing an SMS service.
    """

    def send_sms(self, phone_number: str, message: str) -> None:
        """
        Sends an SMS message.

        Args:
            phone_number (str): The recipient's phone number.
            message (str): The SMS message content.

        Raises:
            ValueError: If the phone number format is invalid.
        """

        if not phone_number.startswith("+"):
            raise ValueError("Invalid phone number format")

        print(f"SMS sent to {phone_number}: {message}")
