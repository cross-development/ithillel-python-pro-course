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
