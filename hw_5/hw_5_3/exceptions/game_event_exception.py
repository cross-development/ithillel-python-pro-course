"""
This module defines a custom exception class, GameEventException,
for representing game events.

GameEventException provides a structured way to encapsulate
information about game events, including the event type and
additional details.
"""

from typing import Dict, Any

from hw_5.hw_5_3.enums.event_type import EventType


class GameEventException(Exception):
    """
    Custom exception raised for game events.
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
