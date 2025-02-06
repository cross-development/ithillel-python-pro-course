"""
This module provides a StringProcessor class with static methods \
for common string manipulations.

- `reverse_string(string)`: Reverses the order of characters in the given string.
- `capitalize_string(string)`: Capitalizes the first character of the string.
- `count_vowels(string)`: Counts the number of vowels within the string.
"""


class StringProcessor:
    """
    A utility class for performing common string operations.
    """

    @staticmethod
    def reverse_string(string: str) -> str:
        """
        Reverses the order of characters in the given string.

        Args:
            string (str): The input string.

        Returns:
            str: The reversed string.
        """

        return string[::-1]

    @staticmethod
    def capitalize_string(string: str) -> str:
        """
        Capitalizes the first character of the string.

        Args:
            string (str): The input string.

        Returns:
            str: The string with the first character capitalized.
        """

        return string.capitalize()

    @staticmethod
    def count_vowels(string: str) -> int:
        """
        Counts the number of vowels within the string.

        Args:
            string (str): The input string.

        Returns:
            str: The number of vowels in the string.
        """

        vowels = "aeiouAEIOU"
        return sum(1 for char in string if char in vowels)
