"""
Module with custom regular expressions for various text-processing tasks.
"""

import re
from typing import List


def find_words_starting_with(text: str, prefix: str) -> List[str]:
    """
    Finds all words in the text that start with a given prefix.

    Args:
        text (str): The input text.
        prefix (str): The prefix to search for.

    Returns:
        List[str]: A list of words that start with the given prefix.
    """

    pattern = rf"\b{re.escape(prefix)}\w*\b"

    return re.findall(pattern, text)


def extract_currency_values(text: str) -> List[str]:
    """
    Extracts currency values in USD format (e.g., $123.45, $1000).

    Args:
        text (str): The text containing currency values.

    Returns:
        List[str]: A list of extracted currency values.
    """

    pattern = r"\$\d+(?:\.\d{2})?"

    return re.findall(pattern, text)


if __name__ == "__main__":
    SAMPLE_TEXT = "Today I spent $10.50 on coffee and $200 on a new phone."
    print("Currency values:", extract_currency_values(SAMPLE_TEXT))

    WORDS_TEXT = "apple banana apricot cherry avocado"
    print("Words starting with 'a':", find_words_starting_with(WORDS_TEXT, "a"))
