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
