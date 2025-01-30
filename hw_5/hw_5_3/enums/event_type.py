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
