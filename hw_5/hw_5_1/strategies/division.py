from decimal import Decimal

from hw_5.hw_5_1.strategies.operational_strategy import OperationalStrategy


class Division(OperationalStrategy):
    """
    Strategy for division operation.
    """

    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Divides one decimal number by another.

        Args:
            a (Decimal): The dividend.
            b (Decimal): The divisor.

        Raises:
            ZeroDivisionError: If the divisor is zero.

        Returns:
            Decimal: The quotient of the two numbers.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return a / b
