"""
This module defines the Player class, representing a player in a game with resources.

The Player class provides methods for:

- Managing the player's resources.
- Checking if the player has enough resources for a specific action.
- Spending resources from the player's inventory.

This class encapsulates player resource management logic and provides
a clear and reusable interface for other game components.
"""

from typing import Dict

from hw_5.hw_5_4.enums.game_resource import GameResource
from hw_5.hw_5_4.exceptions.insufficient_resources_exception import InsufficientResourcesException


class Player:
    """
    Represents a player with resources.
    """

    def __init__(self, resources: Dict[GameResource, int]) -> None:
        """
        Initializes the Player with a dictionary of resources.

        Args:
            resources (Dict[GameResource, int]): A dictionary of the player's resources.
        """
        self.resources = resources

    def get_resource(self, resource: GameResource) -> int:
        """
        Gets the amount of a specific resource the player has.

        Args:
            resource (GameResource): The resource to get the amount of.

        Returns:
            int: The amount of the resource the player has, \
                 or 0 if the player doesn't have the resource.
        """
        return self.resources.get(resource, 0)

    def has_enough_resources(self, resource: GameResource, amount: int) -> bool:
        """
        Checks if the player has enough of a specific resource.

        Args:
            resource (GameResource): The resource to check.
            amount (int): The amount of the resource required.

        Returns:
            bool: True if the player has enough of the resource, False otherwise.
        """
        return self.get_resource(resource) >= amount

    def check_all_resources(self, required_resources: Dict[GameResource, int]) -> None:
        """
        Checks if the player has enough of all required resources.

        Args:
            required_resources (Dict[GameResource, int]): A dictionary of the \
                                                          resources to check and their amounts.

        Raises:
            InsufficientResourcesException: If the player doesn't have enough of any resource.
        """
        for resource, amount in required_resources.items():
            if not self.has_enough_resources(resource, amount):
                raise InsufficientResourcesException(resource, amount, self.get_resource(resource))

    def spend_resources(self, required_resources: Dict[GameResource, int]) -> None:
        """
        Spends resources from the player's resources. \
        All resources are spent only if the player has enough of each resource.

        Args:
            required_resources (Dict[GameResource, int]): A dictionary of the \
                                                          resources to spend and their amounts.

        Raises:
            InsufficientResourcesException: If the player doesn't have enough of any resource.
        """
        self.check_all_resources(required_resources)

        # If we have enough of everything, then spend all resources
        for resource, amount in required_resources.items():
            self.resources[resource] -= amount
