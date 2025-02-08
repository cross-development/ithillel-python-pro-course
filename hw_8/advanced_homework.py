"""
This module implements an EventDispatcher class for managing and dispatching events.
It allows registering event handlers and dispatching events with associated data.
"""

from typing import Callable, Any, Dict, List


class EventDispatcher:
    """
    A class to manage and dispatch events.

    Attributes:
        events (Dict[str, List[Callable[[Any], None]]]): A dictionary mapping event \
                                                         names to lists of event handlers.
    """

    def __init__(self) -> None:
        """
        Initializes the EventDispatcher with an empty dictionary of events.
        """

        self.events: Dict[str, List[Callable[[Any], None]]] = {}

    def register_event(self, name: str, handler: Callable[[Any], None]) -> None:
        """
        Registers an event handler for a specific event.

        Args:
            name (str): The name of the event to register the handler for.
            handler (Callable[[Any], None]): The function to be called when the event is dispatched.
        """

        if name not in self.events:
            self.events[name] = []

        self.events[name].append(handler)

    def dispatch_event(self, name: str, data: Any) -> None:
        """
        Dispatches an event by invoking all registered handlers with the provided data.

        Args:
            name (str): The name of the event to dispatch.
            data (Any): The data to pass to the event handlers.

        Raises:
            Prints a message if the event has no registered handlers.
        """

        if name in self.events:
            for handler in self.events[name]:
                handler(data)
        else:
            print(f"Event '{name}' not registered")


def on_message(data: str) -> None:
    """
    An example event handler that processes string messages.

    Args:
        data (str): The message data received from the event.

    Example:
        >>> on_message("Hello World!")
        Message received: Hello World!
    """

    print(f"Message received: {data}")


def another_handler(data: str) -> None:
    """
    Another example event handler that processes string messages.

    Args:
        data (str): The message data received from the event.

    Example:
        >>> another_handler("Test message!")
        Another handler received: Test message!
    """

    print(f"Another handler received: {data}")


if __name__ == "__main__":
    dispatcher = EventDispatcher()

    # Register and dispatch the "message" event
    dispatcher.register_event("message", on_message)
    dispatcher.dispatch_event("message", "Hello World!")

    # Register and dispatch the "another_message" event
    dispatcher.register_event("another_message", another_handler)
    dispatcher.dispatch_event("another_message", "Test message!")

    # Attempt to dispatch an unregistered event
    dispatcher.dispatch_event("unknown_event", "It won't work!")
