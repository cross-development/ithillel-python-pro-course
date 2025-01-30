from enum import Enum


class TransactionType(Enum):
    """
    Enum representing different transaction types.

    Members:
        WITHDRAW: Withdrawal transaction.
        PURCHASE: Purchase transaction.
        DEPOSIT: Deposit transaction.
    """
    WITHDRAW = 'withdraw'
    PURCHASE = 'purchase'
    DEPOSIT = 'deposit'
