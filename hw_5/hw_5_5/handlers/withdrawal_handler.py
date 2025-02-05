"""
This module defines the WithdrawalHandler class, which extends the TransactionHandler
and is responsible for handling withdrawal transactions.

The WithdrawalHandler processes withdrawal transactions by:

- Withdrawing the requested amount from the account balance.
- Printing a confirmation message with the new balance.

The handler then optionally passes the transaction to the next handler
in the chain for further processing (e.g., logging).
"""

from decimal import Decimal

from hw_5.hw_5_5.models.account import Account
from hw_5.hw_5_5.enums.transaction_type import TransactionType
from hw_5.hw_5_5.handlers.transaction_handler import TransactionHandler


class WithdrawalHandler(TransactionHandler):
    """
    Handler for withdrawal transactions.

    Attributes:
        _next_handler (Optional[TransactionHandler]): The next handler in the chain.
    """

    def handle(self, account: Account, amount: Decimal, transaction_type: TransactionType) -> None:
        """
        Handles a withdrawal transaction.

        Args:
            account (Account): The account to withdraw from.
            amount (Decimal): The amount to withdraw.
            transaction_type (TransactionType): The type of the transaction.
        """
        if transaction_type == TransactionType.WITHDRAW:
            account.withdraw(amount)

            print(f"💸 Withdrawn {amount} {account.currency}. \
                New balance: {account.balance} {account.currency}.")

        super().handle(account, amount, transaction_type)
