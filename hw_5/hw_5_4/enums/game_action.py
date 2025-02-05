"""
This module defines an Enum, GameAction, representing different actions
that can be performed in a game.

The GameAction enum provides a set of named constants for common game actions,
improving code readability and maintainability.
"""

from enum import Enum


class GameAction(Enum):
    """
    Enum representing different game actions.

    Members:
        - BUY_SWORD: Represents the action of buying a sword.
        - BUILD_SHED: Represents the action of building a shed.
        - GROW_PIG: Represents the action of growing a pig.
    """
    BUY_SWORD = "buy_sword"
    BUILD_SHED = "build_shed"
    GROW_PIG = "grow_pig"
