from typing import Dict, Any

from hw_5.hw_5_3.event_types import EventType


class GameEventException(Exception):
    """
    Custom exception raised for game events.

    Args:
        event_type (EventType): The type of the game event.
        details (Dict[str, Any]): Details about the event.
    """

    def __init__(self, event_type: EventType, details: Dict[str, Any]) -> None:
        """
        Initializes the GameEventException.

        Args:
            event_type (EventType): The type of the game event.
            details (Dict[str, Any]): Details about the event.
        """
        self.event_type = event_type
        self.details = details
