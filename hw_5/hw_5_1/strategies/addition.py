"""
This module defines the Addition class, which implements the OperationalStrategy
interface for performing addition operations on Decimal numbers.
"""

from decimal import Decimal

from hw_5.hw_5_1.strategies.operational_strategy import OperationalStrategy


class Addition(OperationalStrategy):
    """
    Strategy for addition operation.
    """

    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Adds two decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The sum of the two numbers.
        """
        return a + b
