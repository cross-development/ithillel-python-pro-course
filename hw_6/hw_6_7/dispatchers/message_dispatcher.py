"""
This module defines the MessageDispatcher class, which provides a central point
for managing and sending messages through multiple communication channels.

The MessageDispatcher:

- Maintains a list of MessageSender adapters.
- Allows dynamic addition of new adapters.
- Sends messages to all registered adapters, ensuring message delivery
  through multiple channels (e.g., email, SMS, push notifications).
- Handles potential exceptions during message delivery from individual adapters.

This class simplifies the process of sending messages to multiple recipients
or through various communication channels while maintaining flexibility and
error handling.
"""

from typing import List

from hw_6.hw_6_7.adapters.message_sender import MessageSender


class MessageDispatcher:
    """
    Class to manage and send messages through multiple adapters.

    Attributes:
        adapters (List[MessageSender]): List of MessageSender adapters.
    """

    def __init__(self):
        """
        Initializes the MessageDispatcher.
        """

        self.adapters: List[MessageSender] = []

    def add_adapter(self, adapter: MessageSender) -> None:
        """
        Adds a message adapter to the dispatcher.

        Args:
            adapter (MessageSender): The message adapter to add.
        """

        self.adapters.append(adapter)

    def send_message_to_all(self, message: str) -> None:
        """
        Sends a message to all registered adapters.

        Args:
            message (str): The message to send.
        """

        for adapter in self.adapters:
            try:
                adapter.send_message(message)
            except Exception as e:
                print(f"Error using adapter {adapter}: {e}")
