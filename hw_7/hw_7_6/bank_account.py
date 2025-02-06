"""
This module defines the BankAccount class, which represents a simple bank account.

- `__init__(initial_balance)`: Initializes a new bank account with an optional initial balance.
- `deposit(amount)`: Deposits the specified amount into the account.
- `withdraw(amount)`: Withdraws the specified amount from the account.
- `get_balance()`: Returns the current balance of the account.

The class includes basic validation checks for deposit and withdrawal amounts.
"""


class BankAccount:
    """
    Represents a simple bank account.
    """

    def __init__(self, initial_balance: float = 0.0) -> None:
        """
        Initializes a new bank account with an optional initial balance.

        Args:
            initial_balance (float): The initial balance of the account (defaults to 0.0).
        """

        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is not positive.
        """

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws the specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is not positive.
            ValueError: If the withdrawal amount exceeds the current balance.
        """

        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """

        return self.balance
