"""
This module provides a utility class for age verification.

- `is_adult(age)`: Checks if a given age is considered adult (18 years or older).
"""


class AgeVerifier:
    """
    A utility class for age verification.
    """

    @staticmethod
    def is_adult(age: int) -> bool:
        """
        Checks if a given age is considered adult (18 years or older).

        Args:
            age (int): The age to be checked.

        Returns:
            bool: True if the age is 18 or older, False otherwise.

        Raises:
            ValueError: If the age is negative.
        """

        if age < 0:
            raise ValueError("Age cannot be negative")

        return age >= 18
