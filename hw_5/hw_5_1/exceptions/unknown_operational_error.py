"""
This module defines a custom exception class, UnknownOperationalError,
to be raised when an unknown arithmetic operation is requested.

This exception can be used to provide more specific and informative error
messages in situations where an unexpected or invalid arithmetic operation
is encountered.
"""


class UnknownOperationalError(Exception):
    """
    Custom exception raised when an unknown arithmetic operation is requested.
    """
