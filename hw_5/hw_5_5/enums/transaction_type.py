"""
This module defines an Enum, TransactionType, representing different
types of financial transactions.

The TransactionType enum provides a set of named constants for common transaction types
such as WITHDRAW, PURCHASE, and DEPOSIT, improving code readability and maintainability.
"""

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
