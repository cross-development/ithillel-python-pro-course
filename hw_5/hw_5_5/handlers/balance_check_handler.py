from decimal import Decimal

from hw_5.hw_5_5.models.account import Account
from hw_5.hw_5_5.enums.transaction_type import TransactionType
from hw_5.hw_5_5.handlers.transaction_handler import TransactionHandler
from hw_5.hw_5_5.exceptions.insufficient_funds_exception import InsufficientFundsException


class BalanceCheckHandler(TransactionHandler):
    """
    Handler that checks if the account has sufficient balance for a transaction.

    Attributes:
        _next_handler (Optional[TransactionHandler]): The next handler in the chain.
    """

    def handle(self, account: Account, amount: Decimal, transaction_type: TransactionType) -> None:
        """
        Handles the transaction by checking the account balance.

        Args:
            account (Account): The account to check.
            amount (Decimal): The amount of the transaction.
            transaction_type (TransactionType): The type of the transaction.

        Raises:
            InsufficientFundsException: If the account balance is insufficient.
        """
        if transaction_type in [TransactionType.PURCHASE, TransactionType.WITHDRAW]:
            if account.balance < amount:
                raise InsufficientFundsException(amount, account.balance, account.currency, transaction_type)

        print(f"✅ Balance check passed for {transaction_type.value}: {amount} {account.currency}.")

        super().handle(account, amount, transaction_type)
