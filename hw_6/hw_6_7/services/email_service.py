"""
This module defines the EmailService class, which simulates the functionality
of an email sending service.

The EmailService provides a `send_email` method that:

- Takes the recipient's email address and the message content as input.
- Performs basic validation of the email address.
- Simulates sending the email by printing a confirmation message.

This class can be used as a placeholder or for testing purposes
before integrating with a real email sending library.
"""


class EmailService:
    """
    Class representing an email service.
    """

    def send_email(self, email_address: str, message: str) -> None:
        """
        Sends an email.

        Args:
            email_address (str): The recipient's email address.
            message (str): The email message content.

        Raises:
            ValueError: If the email address is invalid.
        """

        if "@" not in email_address:
            raise ValueError("Invalid email address format")

        print(f"Email sent to {email_address}: {message}")
