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

        pass
