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
