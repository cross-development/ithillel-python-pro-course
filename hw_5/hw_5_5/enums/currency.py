"""
This module defines an Enum, Currency, representing different currencies.

The Currency enum provides a set of named constants for common currencies
such as USD, EUR, and UAH, improving code readability and maintainability.
"""

from enum import Enum


class Currency(Enum):
    """
    Enum representing different currencies.

    Members:
        USD: United States Dollar.
        EUR: Euro.
        UAH: Ukrainian Hryvnia.
    """
    USD = 'USD'
    EUR = 'EUR'
    UAH = 'UAH'
