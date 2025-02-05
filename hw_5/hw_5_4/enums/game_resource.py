"""
This module defines an Enum, GameResource, representing different
resources available in a game.

The GameResource enum provides a set of named constants for common game resources
such as GOLD, WOOD, STONE, and FOOD, improving code readability and maintainability.
"""

from enum import Enum


class GameResource(Enum):
    """
    Enum representing different game resources.

    Members:
        - GOLD: Represents gold resource.
        - WOOD: Represents wood resource.
        - STONE: Represents stone resource.
        - FOOD: Represents food resource.
    """
    GOLD = "gold"
    WOOD = "wood"
    STONE = "stone"
    FOOD = "food"
