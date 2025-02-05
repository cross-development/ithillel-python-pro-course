"""
This module defines the Transaction class, representing a financial transaction.

The Transaction class encapsulates information about:

- The type of transaction (e.g., withdrawal, deposit, purchase).
- The amount involved in the transaction.

This class provides a structured way to represent and handle
transactions within the financial system.
"""

from decimal import Decimal

from hw_5.hw_5_5.enums.transaction_type import TransactionType


class Transaction:
    """
    Represents a financial transaction.
    """

    def __init__(self, transaction_type: TransactionType, amount: Decimal) -> None:
        """
        Initializes the Transaction.

        Args:
            transaction_type (TransactionType): The type of the transaction.
            amount (Decimal): The amount of the transaction.
        """
        self.transaction_type = transaction_type
        self.amount = amount
