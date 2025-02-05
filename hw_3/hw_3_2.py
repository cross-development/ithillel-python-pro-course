"""
This module defines a Vector class representing a mathematical vector in n-dimensional space.

The Vector class provides methods for:

- Creating Vector objects.
- Performing vector operations: addition, subtraction, scalar multiplication.
- Calculating the length (magnitude) of the vector.
- Comparing vectors: equality and less-than comparison based on length.
- String representation of the vector.

The module includes unit tests to verify the correctness of the implemented operations.
"""

from math import sqrt


class Vector:
    """
    Represents a mathematical vector in n-dimensional space.

    Attributes:
        components (list): A list of numerical values representing the components of the vector.
    """

    def __init__(self, components: list[int | float]) -> None:
        """
        Initializes a Vector object.

        Args:
            components (list): A list of numerical values representing the
                              components of the vector.
        """
        self.components = components

    def length(self) -> float:
        """
        Calculates the Euclidean length (magnitude) of the vector.

        Returns:
            float: The length of the vector.
        """
        return sqrt(sum(x ** 2 for x in self.components))

    def __add__(self, other: 'Vector') -> 'Vector':
        """
       Adds two vectors together.

       Args:
           other (Vector): The other vector to add.

       Raises:
           ValueError: If the vectors have different dimensions.

       Returns:
           Vector: The resulting vector after addition.
       """
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions to add.")

        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Subtracts one vector from another.

        Args:
            other (Vector): The vector to subtract.

        Raises:
            ValueError: If the vectors have different dimensions.

        Returns:
            Vector: The resulting vector after subtraction.
        """
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions to subtract.")

        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar: int | float) -> 'Vector':
        """
        Multiplies the vector by a scalar value.

        Args:
            scalar (int or float): The scalar value to multiply by.

        Returns:
            Vector: The resulting vector after scalar multiplication.
        """
        return Vector([x * scalar for x in self.components])

    def __eq__(self, other: 'Vector') -> bool:
        """
        Checks if two vectors are equal.

        Args:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if the vectors are equal, False otherwise.
        """
        return self.components == other.components

    def __lt__(self, other: 'Vector') -> bool:
        """
        Compares the lengths of two vectors.

        Args:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if the length of this vector is less than the length of
                 the other vector, False otherwise.
        """
        return self.length() < other.length()

    def __repr__(self) -> str:
        """
        Returns a string representation of the vector.

        Returns:
            str: The string representation of the vector.
        """
        return f"Vector({self.components})"


v1 = Vector([3, 4])
v2 = Vector([1, 2])

v3 = v1 + v2
print(v3)
assert str(v3) == "Vector([4, 6])", "The result of adding should be a new Vector([4, 6])"

v4 = v1 - v2
print(v4)
assert str(v4) == "Vector([2, 2])", "The result of subtracting should be a Vector([2, 2])"

v5 = v1 * 2
print(v5)
assert str(v5) == "Vector([6, 8])", "The result of multiplying should be a new Vector([6, 8])"

print(v1.length())
assert v1.length() == 5.0, "The length of the vector Vector([3, 4]) should be 5.0"

print(v1 < v2)
assert (v1 < v2) is False, "Vector([3, 4]) should be greater than Vector([1, 2])"

print(v1 == Vector([3, 4]))
assert (v1 == Vector([3, 4])) is True, "Vector([3, 4]) and Vector([3, 4]) should be equal"

print("All tests passed!")
