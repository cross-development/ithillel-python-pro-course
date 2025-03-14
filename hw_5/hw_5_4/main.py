"""
This module provides a simple demonstration of the request handling system.

It creates a Player object, initializes a ResourceCheckHandler,
and simulates a series of game actions (requests) to be processed
by the handler. This demonstrates the basic workflow of the request
handling system and how the ResourceCheckHandler verifies
player resources before proceeding with the action.
"""

from hw_5.hw_5_4.enums.game_action import GameAction
from hw_5.hw_5_4.enums.game_resource import GameResource
from hw_5.hw_5_4.models.player import Player
from hw_5.hw_5_4.models.request import Request
from hw_5.hw_5_4.handlers.resource_check_handler import ResourceCheckHandler

if __name__ == '__main__':
    player = Player(resources={
        GameResource.GOLD: 100,
        GameResource.WOOD: 50,
        GameResource.STONE: 20,
        GameResource.FOOD: 10,
    })

    resource_check = ResourceCheckHandler()

    actions = [
        Request(GameAction.BUY_SWORD, {GameResource.GOLD: 50}),
        Request(GameAction.BUILD_SHED, {GameResource.WOOD: 50, GameResource.STONE: 30}),
        Request(GameAction.GROW_PIG, {GameResource.FOOD: 5}),
    ]

    for action in actions:
        resource_check.handle(player, action)
