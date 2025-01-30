from typing import Dict
from decimal import Decimal, InvalidOperation

from hw_5.hw_5_1.strategies.operational_strategy import OperationalStrategy
from hw_5.hw_5_1.strategies.addition import Addition
from hw_5.hw_5_1.strategies.division import Division
from hw_5.hw_5_1.strategies.subtraction import Subtraction
from hw_5.hw_5_1.strategies.multiplication import Multiplication
from hw_5.hw_5_1.exceptions.unknown_operational_error import UnknownOperationalError


class Calculator:
    """
    A calculator class that performs arithmetic operations based on a given strategy.

    Attributes:
        operations (Dict[str, OperationStrategy]): A dictionary mapping operators to their corresponding strategies.
    """

    def __init__(self) -> None:
        """
        Initializes the Calculator with a dictionary of supported operations.
        """
        self.operations: Dict[str, OperationalStrategy] = {
            "+": Addition(),
            "-": Subtraction(),
            "*": Multiplication(),
            "/": Division(),
        }

    def calculate(self, a: str, operator: str, b: str) -> Decimal:
        """
        Performs a calculation based on the given operands and operator.

        Args:
            a (str): The first operand as a string.
            operator (str): The arithmetic operator.
            b (str): The second operand as a string.

        Raises:
            UnknownOperationError: If the operator is not supported.
            ValueError: If the operands cannot be converted to decimal numbers.
            ZeroDivisionError: If division by zero is attempted.
            OverflowError: If the result of the calculation is too large.

        Returns:
            Decimal: The result of the calculation.
        """
        try:
            a_decimal = Decimal(a)
            b_decimal = Decimal(b)

            if operator not in self.operations:
                raise UnknownOperationalError(f"Unknown operation: {operator}")

            result = self.operations[operator].execute(a_decimal, b_decimal)

            if result.is_infinite():
                raise OverflowError("Result is too large to handle.")

            return result
        except InvalidOperation:
            raise ValueError("Invalid number format. Please enter valid decimal numbers.")
        except ZeroDivisionError as e:
            raise ZeroDivisionError(e)
        except OverflowError as e:
            raise OverflowError(e)
