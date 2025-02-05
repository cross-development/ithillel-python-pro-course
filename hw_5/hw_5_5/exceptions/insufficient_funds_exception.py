"""
This module defines a custom exception, InsufficientFundsException,
specifically for handling cases where an account lacks sufficient funds
to complete a requested transaction.

The exception provides detailed information about the transaction
(type, required amount, current balance, and currency),
making it easier to diagnose and handle insufficient funds situations.
"""

from decimal import Decimal

from hw_5.hw_5_5.enums.currency import Currency
from hw_5.hw_5_5.enums.transaction_type import TransactionType


class InsufficientFundsException(Exception):
    """
    Exception raised when an account has insufficient funds for a transaction.
    """

    def __init__(self,
                 required_amount: Decimal,
                 current_balance: Decimal,
                 currency: Currency,
                 transaction_type: TransactionType) -> None:
        """
        Initializes the InsufficientFundsException.

        Args:
            required_amount (Decimal): The required amount for the transaction.
            current_balance (Decimal): The current balance of the account.
            currency (Currency): The currency of the account.
            transaction_type (TransactionType): The type of the transaction.
        """
        super().__init__(
            f"Insufficient funds for {transaction_type.value}. \
            Required: {required_amount} {currency.value}, \
            current balance: {current_balance} {currency.value}")

        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type
