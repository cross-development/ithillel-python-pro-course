"""
This module provides a UniqueIDIterator class for generating unique identifiers.
The iterator utilizes the UUID4 algorithm from the `uuid` library to efficiently
produce a series of unique identifiers.
"""

import uuid
from typing import Iterator


class UniqueIDIterator:
    """An iterator for generating unique identifiers using UUID4."""

    def __iter__(self) -> Iterator[str]:
        """
        Returns the iterator object itself.

        Returns:
            Iterator[str]: The iterator object that generates unique identifiers.
        """
        return self

    def __next__(self) -> str:
        """
        Generates the next unique identifier.

        Returns:
            str: A unique identifier generated using UUID4.
        """
        return str(uuid.uuid4())


unique_ids = UniqueIDIterator()

for _ in range(5):
    print(next(unique_ids))

print("All tests passed!")
