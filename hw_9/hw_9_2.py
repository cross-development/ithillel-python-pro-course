"""
Module for extracting phone numbers from text using regular expressions.
"""

import re
from typing import List


def find_phone_numbers(text: str) -> List[str]:
    """
    Extracts all phone numbers from the given text.

    Args:
        text (str): The text containing phone numbers.

    Returns:
        List[str]: A list of found phone numbers.
    """

    pattern = r"\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}"

    return re.findall(pattern, text)


if __name__ == "__main__":
    SAMPLE_TEXT = "Call me at (123) 456-7890 or 987-654-3210. My old number was 555.123.4567."

    print(find_phone_numbers(SAMPLE_TEXT))
