"""
This module defines the Request class, representing a player's request
to perform an action within the game.

The Request object encapsulates information about:

- The specific action the player wants to perform (e.g., BUY_SWORD, BUILD_SHED).
- The resources required to execute the action.

This class provides a structured way to represent and handle player actions
within the game logic.
"""

from typing import Dict

from hw_5.hw_5_4.enums.game_action import GameAction
from hw_5.hw_5_4.enums.game_resource import GameResource


class Request:
    """
    Represents a player's request to perform a game action.
    """

    def __init__(self, action_name: GameAction, required_resources: Dict[GameResource, int]) -> None:
        """
        Initializes the Request object.

        Args:
            action_name (GameAction): The name of the action to perform.
            required_resources (Dict[GameResource, int]): A dictionary of the \
                                                resources required to perform the action.
        """
        self.action_name = action_name
        self.required_resources = required_resources
