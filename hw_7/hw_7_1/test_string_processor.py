"""
This module contains unit tests for the StringProcessor class.

The tests cover the following methods:

- `test_reverse_string_empty`: Tests the behavior of `reverse_string` with an empty string.
- `test_reverse_string`: Tests the `reverse_string` method with various input strings.
- `test_capitalize_string`: Tests the `capitalize_string` method with different inputs.
- `test_count_vowels`: Tests the `count_vowels` method with various inputs.
"""

import unittest

from hw_7.hw_7_1.string_processor import StringProcessor


class TestStringProcessor(unittest.TestCase):
    """
    Unit tests for the StringProcessor class.
    """

    @unittest.skip("Skip test for an empty string")
    def test_reverse_string_empty(self) -> None:
        """
        Tests the `reverse_string` method with an empty string.
        """

        self.assertEqual(StringProcessor.reverse_string(""), "")

    def test_reverse_string(self) -> None:
        """
        Tests the `reverse_string` method with various input strings.
        """

        self.assertEqual(StringProcessor.reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(StringProcessor.reverse_string("Python"), "nohtyP")
        self.assertEqual(StringProcessor.reverse_string("12345"), "54321")

    def test_capitalize_string(self) -> None:
        """
        Tests the `capitalize_string` method with different inputs.
        """

        self.assertEqual(StringProcessor.capitalize_string("hello world"), "Hello world")
        self.assertEqual(StringProcessor.capitalize_string("python"), "Python")
        self.assertEqual(StringProcessor.capitalize_string("123abc"), "123abc")

    def test_count_vowels(self) -> None:
        """
        Tests the `count_vowels` method with various inputs.
        """

        self.assertEqual(StringProcessor.count_vowels("hello world"), 3)
        self.assertEqual(StringProcessor.count_vowels("PYTHON"), 1)
        self.assertEqual(StringProcessor.count_vowels("bcdfg"), 0)
        self.assertEqual(StringProcessor.count_vowels("aeiouAEIOU"), 10)


if __name__ == "__main__":
    unittest.main()
