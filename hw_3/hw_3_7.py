import math


class Vector:
    """
    Represents a vector in n-dimensional space.

    Attributes:
        coordinates (list): A list of floating-point numbers representing the  coordinates of the vector.
    """

    def __init__(self, coordinates: list[float]):
        """
        Initializes a Vector object.

        Args:
            coordinates (list): A list of floating-point numbers representing the coordinates of the vector.
        """
        self.coordinates = coordinates

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
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have the same dimension for addition.")

        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Subtracts one vector from another.

        Args:
            other (Vector): The other vector to subtract.

        Raises:
            ValueError: If the vectors have different dimensions.

        Returns:
            Vector: The resulting vector after subtraction.
        """
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have the same dimension for subtraction.")

        return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])

    def __mul__(self, other: 'Vector') -> float:
        """
        Calculates the dot product (scalar product) of two vectors.

        Args:
            other (Vector): The other vector for the dot product.

        Raises:
            ValueError: If the vectors have different dimensions.

        Returns:
            float: The dot product of the two vectors.
        """
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have the same dimension for dot product.")

        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))

    def __eq__(self, other: 'Vector') -> bool:
        """
        Checks if two vectors have the same magnitude.

        Args:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if the magnitudes of the vectors are equal, False otherwise.
        """
        return math.isclose(self.magnitude(), other.magnitude())

    def __lt__(self, other: 'Vector') -> bool:
        """
        Compares the magnitudes of two vectors.

        Args:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if the magnitude of this vector is less than the magnitude of the other vector, False otherwise.
        """
        return self.magnitude() < other.magnitude()

    def __gt__(self, other: 'Vector') -> bool:
        """
        Compares the magnitudes of two vectors.

        Args:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if the magnitude of this vector is greater than the magnitude of the other vector, False otherwise.
        """
        return self.magnitude() > other.magnitude()

    def magnitude(self) -> float:
        """
        Calculates the magnitude (length) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return math.sqrt(sum(x ** 2 for x in self.coordinates))

    def __repr__(self) -> str:
        """
        Returns a string representation of the vector.

        Returns:
            str: The string representation of the vector.
        """
        return f"Vector({self.coordinates})"


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Vectors:")
print(f"v1 = {v1}")
assert str(v1) == "Vector([1, 2, 3])", "v1 should be Vector([1, 2, 3])"
print(f"v2 = {v2}")
assert str(v2) == "Vector([4, 5, 6])", "v1 should be Vector([4, 5, 6])"

print("\nOperations:")
print(f"Sum: v1 + v2 = {v1 + v2}")
assert str(v1 + v2) == "Vector([5, 7, 9])", "Sum of v1 and v2 should be Vector([5, 7, 9])"
print(f"Difference: v1 - v2 = {v1 - v2}")
assert str(v1 - v2) == "Vector([-3, -3, -3])", "Difference between v1 and v2 should be Vector([-3, -3, -3])"
print(f"Dot product: v1 * v2 = {v1 * v2}")
assert v1 * v2 == 32, "Dot product of v1 and v2 should be 32"

print("\nComparisons:")
print(f"v1 == v2: {v1 == v2}")
assert (v1 == v2) == False, "v1 should not be equal to v2"
print(f"v1 < v2: {v1 < v2}")
assert (v1 < v2) == True, "v1 should not be greater than v2"
print(f"v1 > v2: {v1 > v2}")
assert (v1 > v2) == False, "v2 should be greater than v1"

print("All tests passed!")
