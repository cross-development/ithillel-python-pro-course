from hw_5.hw_5_4.models.player import Player
from hw_5.hw_5_4.models.request import Request
from hw_5.hw_5_4.handlers.base_handler import BaseHandler
from hw_5.hw_5_4.exceptions.insufficient_resources_exception import InsufficientResourcesException


class ResourceCheckHandler(BaseHandler):
    """
    Handler that checks if the player has enough resources to fulfill the request.
    """

    def handle(self, player: Player, request: Request) -> None:
        """
        Handles the request by checking resources and performing the action.

        Args:
            player (Player): The player making the request.
            request (Request): The request to handle.
        """
        try:
            player.spend_resources(request.required_resources)
            print(f"✅ Action '{request.action_name.value}' successfully performed!")
        except InsufficientResourcesException as e:
            print(f"❌ {e}")

        super().handle(player, request)
