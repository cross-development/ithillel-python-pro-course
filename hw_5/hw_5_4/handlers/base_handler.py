from typing import Optional
from abc import ABC, abstractmethod

from hw_5.hw_5_4.models.player import Player
from hw_5.hw_5_4.models.request import Request


class BaseHandler(ABC):
    """
    Abstract base class for request handlers.

    Attributes:
        _next_handler (Optional[BaseHandler]): The next handler in the chain.
    """

    def __init__(self) -> None:
        """
        Initializes the BaseHandler.
        """
        self._next_handler: Optional["BaseHandler"] = None

    def set_next(self, handler: "BaseHandler") -> "BaseHandler":
        """
        Sets the next handler in the chain.

        Args:
            handler (BaseHandler): The next handler.

        Returns:
            BaseHandler: The current handler.
        """
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, player: Player, request: Request) -> None:
        """
        Handles the request.

        Args:
            player (Player): The player making the request.
            request (Request): The request to handle.
        """
        if self._next_handler:
            self._next_handler.handle(player, request)
