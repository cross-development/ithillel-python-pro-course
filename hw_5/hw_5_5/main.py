from decimal import Decimal

from hw_5.hw_5_5.models.account import Account
from hw_5.hw_5_5.models.transaction import Transaction
from hw_5.hw_5_5.enums.currency import Currency
from hw_5.hw_5_5.enums.transaction_type import TransactionType
from hw_5.hw_5_5.handlers.balance_check_handler import BalanceCheckHandler
from hw_5.hw_5_5.handlers.deposit_handler import DepositHandler
from hw_5.hw_5_5.handlers.purchase_handler import PurchaseHandler
from hw_5.hw_5_5.handlers.withdrawal_handler import WithdrawalHandler
from hw_5.hw_5_5.exceptions.insufficient_funds_exception import InsufficientFundsException

if __name__ == '__main__':
    account = Account(balance=Decimal(100), currency=Currency.USD)

    balance_check = BalanceCheckHandler()
    withdrawal_handler = WithdrawalHandler()
    purchase_handler = PurchaseHandler()
    deposit_handler = DepositHandler()

    balance_check.set_next(withdrawal_handler).set_next(purchase_handler).set_next(deposit_handler)

    transactions = [
        Transaction(TransactionType.DEPOSIT, Decimal(50)),
        Transaction(TransactionType.WITHDRAW, Decimal(30)),
        Transaction(TransactionType.PURCHASE, Decimal(80)),
        Transaction(TransactionType.WITHDRAW, Decimal(50)),
    ]

    for transaction in transactions:
        try:
            balance_check.handle(account, transaction.amount, transaction.transaction_type)
        except InsufficientFundsException as e:
            print(f"❌ {e}")
