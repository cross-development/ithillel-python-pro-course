from typing import Optional
from decimal import Decimal
from abc import ABC, abstractmethod

from hw_5.hw_5_5.models.account import Account
from hw_5.hw_5_5.enums.transaction_type import TransactionType


class TransactionHandler(ABC):
    """
    Abstract base class for transaction handlers.

    Attributes:
        _next_handler (Optional[TransactionHandler]): The next handler in the chain.
    """

    def __init__(self) -> None:
        """
        Initializes the TransactionHandler.
        """
        self._next_handler: Optional['TransactionHandler'] = None

    def set_next(self, handler: 'TransactionHandler') -> 'TransactionHandler':
        """
        Sets the next handler in the chain.

        Args:
            handler (TransactionHandler): The next handler.

        Returns:
            TransactionHandler: The current handler.
        """
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, account: Account, amount: Decimal, transaction_type: TransactionType) -> None:
        """
        Handles the transaction.

        Args:
            account (Account): The account to process the transaction on.
            amount (Decimal): The amount of the transaction.
            transaction_type (TransactionType): The type of the transaction.
        """
        if self._next_handler:
            self._next_handler.handle(account, amount, transaction_type)
