from decimal import Decimal

from hw_5.hw_5_5.models.account import Account
from hw_5.hw_5_5.enums.transaction_type import TransactionType
from hw_5.hw_5_5.handlers.transaction_handler import TransactionHandler


class PurchaseHandler(TransactionHandler):
    """
    Handler for purchase transactions.

    Attributes:
        _next_handler (Optional[TransactionHandler]): The next handler in the chain.
    """

    def handle(self, account: Account, amount: Decimal, transaction_type: TransactionType) -> None:
        """
        Handles a purchase transaction.

        Args:
            account (Account): The account to purchase from.
            amount (Decimal): The amount of the purchase.
            transaction_type (TransactionType): The type of the transaction.
        """
        if transaction_type == TransactionType.PURCHASE:
            account.withdraw(amount)

            print(f"🛒 Successful purchase for {amount} {account.currency}.")

        super().handle(account, amount, transaction_type)
