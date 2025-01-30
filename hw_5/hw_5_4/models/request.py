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
            required_resources (Dict[GameResource, int]): A dictionary of the resources required to perform the action.
        """
        self.action_name = action_name
        self.required_resources = required_resources
