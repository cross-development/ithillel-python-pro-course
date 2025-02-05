"""
This module defines the Multiplication class, which implements the OperationalStrategy
interface for performing multiplication operations on Decimal numbers.
"""

from decimal import Decimal

from hw_5.hw_5_1.strategies.operational_strategy import OperationalStrategy


class Multiplication(OperationalStrategy):
    """
    Strategy for multiplication operation.
    """

    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Multiplies two decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The product of the two numbers.
        """
        return a * b
