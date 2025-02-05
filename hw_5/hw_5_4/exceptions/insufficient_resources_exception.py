"""
This module defines a custom exception, InsufficientResourcesException,
specifically for handling cases where a player lacks the necessary resources
to perform a certain action in a game.

The exception provides information about the missing resource,
the required amount, and the current amount available.
"""

from hw_5.hw_5_4.enums.game_resource import GameResource


class InsufficientResourcesException(Exception):
    """
    Exception raised when a player has insufficient resources to perform an action.
    """

    def __init__(self, required_resource: GameResource, required_amount: int, current_amount: int) -> None:
        """
        Initializes the InsufficientResourcesException.

        Args:
            required_resource (GameResource): The resource that is insufficient.
            required_amount (int): The required amount of the resource.
            current_amount (int): The current amount of the resource the player has.
        """
        super().__init__(
            f"Not enough {required_resource.value}: Required {required_amount}, \
            but only {current_amount} available.")

        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
