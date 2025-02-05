"""
This module defines an Enum, EventType, representing different types of events.

The EventType enum provides a set of named constants for common game events
such as DEATH and LEVEL_UP, improving code readability and maintainability.
"""

from enum import Enum


class EventType(Enum):
    """
    Enum representing different types of game events.

    Members:
        - DEATH: Represents a death event.
        - LEVEL_UP: Represents a level up event.
    """
    DEATH = "death"
    LEVEL_UP = "level_up"
