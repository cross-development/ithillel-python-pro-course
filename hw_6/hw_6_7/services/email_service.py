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
