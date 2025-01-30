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
