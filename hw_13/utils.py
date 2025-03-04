"""
Utility module.
This module provides utility functions for validating URLs and filtering out invalid ones.
"""

from urllib.parse import urlparse
from typing import List, Tuple, Union, overload
from hw_13.logger_config import logging

logger = logging.getLogger(__name__)


def is_valid_url(url: str) -> bool:
    """
    Checks if a given string is a valid URL.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL is valid, otherwise False.
    """

    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


@overload
def validate_urls(urls: List[str]) -> List[str]:
    """
    Overload for validating a list of string URLs.
    """


@overload
def validate_urls(urls: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """
    Overload for validating a list of (URL, filename) tuples.
    """


def validate_urls(urls: Union[List[str], List[Tuple[str, str]]]) -> Union[List[str], List[Tuple[str, str]]]:
    """
    Filters a list of URLs or (URL, filename) tuples, keeping only valid URLs.

    Args:
        urls (Union[List[str], List[Tuple[str, str]]]): A list of URLs or (URL, filename) tuples.

    Returns:
        Union[List[str], List[Tuple[str, str]]]: A list containing only valid URLs or valid (URL, filename) pairs.
    """

    if urls and isinstance(urls[0], str):
        return [url for url in urls if is_valid_url(url)]

    elif urls and isinstance(urls[0], tuple):
        return [(url, filename) for url, filename in urls if is_valid_url(url)]

    return []
