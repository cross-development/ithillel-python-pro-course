"""
This module defines a BinaryNumber class for representing and manipulating binary numbers.

The BinaryNumber class provides methods for:

- Creating BinaryNumber objects.
- Performing bitwise operations: AND, OR, XOR, NOT.
- Representing the BinaryNumber object as a string in binary format.

The module includes unit tests to verify the correctness of the implemented bitwise operations.
"""


class BinaryNumber:
    """
    Represents a binary number.

    Attributes:
        value (int): The integer value of the binary number.
    """

    def __init__(self, value: int) -> None:
        """
        Initializes a BinaryNumber object.

        Args:
            value (int): The integer value of the binary number.

        Raises:
            ValueError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")

        self.value = value

    def __and__(self, other: 'BinaryNumber') -> 'BinaryNumber':
        """
        Performs bitwise AND operation with another BinaryNumber.

        Args:
            other (BinaryNumber): The other BinaryNumber for the operation.

        Returns:
            BinaryNumber: The result of the bitwise AND operation.
        """
        return BinaryNumber(self.value & other.value)

    def __or__(self, other: 'BinaryNumber') -> 'BinaryNumber':
        """
        Performs bitwise OR operation with another BinaryNumber.

        Args:
            other (BinaryNumber): The other BinaryNumber for the operation.

        Returns:
            BinaryNumber: The result of the bitwise OR operation.
        """
        return BinaryNumber(self.value | other.value)

    def __xor__(self, other: 'BinaryNumber') -> 'BinaryNumber':
        """
        Performs bitwise XOR operation with another BinaryNumber.

        Args:
            other (BinaryNumber): The other BinaryNumber for the operation.

        Returns:
            BinaryNumber: The result of the bitwise XOR operation.
        """
        return BinaryNumber(self.value ^ other.value)

    def __invert__(self) -> 'BinaryNumber':
        """
        Performs bitwise NOT operation on the BinaryNumber.

        Returns:
            BinaryNumber: The result of the bitwise NOT operation.
        """
        return BinaryNumber(~self.value)

    def __repr__(self) -> str:
        """
        Returns a string representation of the BinaryNumber.

        Returns:
            str: The string representation of the BinaryNumber in binary format.
        """
        return f"BinaryNumber({bin(self.value)})"


a = BinaryNumber(0b1010)  # 10 in decimal
b = BinaryNumber(0b1100)  # 12 in decimal

print((a & b).value)
assert (a & b).value == 0b1000, "The result of AND operation should be 0b1000"

print((a | b).value)
assert (a | b).value == 0b1110, "The result of OR operation should be 0b1110"

print((a ^ b).value)
assert (a ^ b).value == 0b0110, "The result of XOR operation should be 0b0110"

print((~a).value)
assert (~a).value == -0b1011, "The result of NOT operation should be -0b1011"

print("All tests passed!")
