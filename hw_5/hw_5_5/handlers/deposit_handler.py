from decimal import Decimal

from hw_5.hw_5_5.models.account import Account
from hw_5.hw_5_5.enums.transaction_type import TransactionType
from hw_5.hw_5_5.handlers.transaction_handler import TransactionHandler


class DepositHandler(TransactionHandler):
    """
    Handler for deposit transactions.

    Attributes:
        _next_handler (Optional[TransactionHandler]): The next handler in the chain.
    """

    def handle(self, account: Account, amount: Decimal, transaction_type: TransactionType) -> None:
        """
        Handles a deposit transaction.

        Args:
            account (Account): The account to deposit to.
            amount (Decimal): The amount to deposit.
            transaction_type (TransactionType): The type of the transaction.
        """
        if transaction_type == TransactionType.DEPOSIT:
            account.deposit(amount)

            print(f"💰 Deposited {amount} {account.currency}. New balance: {account.balance} {account.currency}.")

        super().handle(account, amount, transaction_type)
