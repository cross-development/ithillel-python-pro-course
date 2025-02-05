"""
This module defines an abstract base class, OperationalStrategy,
for defining strategies for various arithmetic operations.

The OperationalStrategy class provides a common interface for all
concrete operation strategies, ensuring consistent method signatures
and allowing for easy swapping of different operation strategies.
"""

from decimal import Decimal
from abc import ABC, abstractmethod


class OperationalStrategy(ABC):
    """
    Abstract base class for defining operation strategies.
    """

    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Executes the operation on two decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of the operation.
        """
        pass
