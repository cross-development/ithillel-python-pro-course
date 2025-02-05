"""
This module defines the Account class, representing a bank account.

The Account class provides methods for:

- Managing the account balance.
- Performing deposit and withdrawal operations.

This class encapsulates the core logic for managing account balances
and provides a clear and reusable interface for other parts of the
banking system.
"""

from decimal import Decimal

from hw_5.hw_5_5.enums.currency import Currency


class Account:
    """
    Represents a bank account.
    """

    def __init__(self, balance: Decimal, currency: Currency) -> None:
        """
        Initializes the Account.

        Args:
            balance (Decimal): The initial balance of the account.
            currency (Currency): The currency of the account.
        """
        self.balance = balance
        self.currency = currency

    def withdraw(self, amount: Decimal) -> None:
        """
        Withdraws an amount from the account balance.

        Args:
            amount (Decimal): The amount to withdraw.
        """
        self.balance -= amount

    def deposit(self, amount: Decimal) -> None:
        """
        Deposits an amount into the account balance.

        Args:
            amount (Decimal): The amount to deposit.
        """
        self.balance += amount
