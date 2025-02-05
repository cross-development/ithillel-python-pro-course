"""
This module defines a Fraction class representing mathematical fractions.

The Fraction class provides methods for:

- Creating Fraction objects.
- Performing arithmetic operations (addition, subtraction, multiplication, division) on fractions.
- Representing the Fraction object as a string.

The module includes unit tests to verify the correctness of the implemented operations.
"""

from math import gcd


class Fraction:
    """
    Represents a mathematical fraction.

    Attributes:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction.
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Initializes a Fraction object.

        Args:
            numerator (int): The numerator of the fraction.
            denominator (int): The denominator of the fraction.

        Raises:
            ValueError: If the denominator is zero.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Adds two Fraction objects.

        Args:
            other (Fraction): The other Fraction object to add.

        Returns:
            Fraction: The sum of the two fractions.
        """
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Subtracts one Fraction object from another.

        Args:
            other (Fraction): The Fraction object to subtract.

        Returns:
            Fraction: The difference of the two fractions.
        """
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Multiplies two Fraction objects.

        Args:
            other (Fraction): The other Fraction object to multiply.

        Returns:
            Fraction: The product of the two fractions.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """
        Divides one Fraction object by another.

        Args:
            other (Fraction): The Fraction object to divide by.

        Raises:
            ValueError: If the denominator of the other Fraction is zero.

        Returns:
            Fraction: The quotient of the two fractions.
        """
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return Fraction(new_numerator, new_denominator)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Fraction object.

        Returns:
            str: The string representation of the Fraction object.
        """
        return f"{self.numerator}/{self.denominator}"


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

result_add = fraction1 + fraction2
print(result_add)
assert str(result_add) == "5/4", "The result of adding two fractions should be 5/4"

result_sub = fraction1 - fraction2
print(result_sub)
assert str(result_sub) == "-1/4", "The result of subtracting two fractions should be -1/4"

result_mul = fraction1 * fraction2
print(result_mul)
assert str(result_mul) == "3/8", "The result of multiplying two fractions should be 3/8"

result_div = fraction1 / fraction2
print(result_div)
assert str(result_div) == "2/3", "The result of dividing two fractions should be 2/3"

print("All tests passed!")
