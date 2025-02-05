"""
This module defines the SmsService class, which simulates the functionality
of an SMS sending service.

The SmsService provides a `send_sms` method that:

- Takes the recipient's phone number and the SMS message content as input.
- Performs basic validation of the phone number format.
- Simulates sending the SMS by printing a confirmation message.

This class can be used as a placeholder or for testing purposes
before integrating with a real SMS sending service.
"""


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
