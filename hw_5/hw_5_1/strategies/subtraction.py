from decimal import Decimal

from hw_5.hw_5_1.strategies.operational_strategy import OperationalStrategy


class Subtraction(OperationalStrategy):
    """
    Strategy for subtraction operation.
    """

    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Subtracts one decimal number from another.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The difference between the two numbers.
        """
        return a - b
