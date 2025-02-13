"""
Module for extracting hashtags from text using regular expressions.
"""

import re
from typing import List


def extract_hashtags(text: str) -> List[str]:
    """
    Extracts all hashtags from the given text.

    Args:
        text (str): The input text.

    Returns:
        List[str]: A list of hashtags found in the text.
    """

    pattern = r"#\w+"

    return re.findall(pattern, text)


if __name__ == "__main__":
    SAMPLE_TEXT = "Loving this day! #sunny #happy #weekend"

    print(extract_hashtags(SAMPLE_TEXT))
