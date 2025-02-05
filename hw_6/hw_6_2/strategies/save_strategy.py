"""
This module defines the SaveStrategy abstract base class.

The SaveStrategy interface defines a common method, `save(content, filename)`,
for saving content to a file using different strategies (e.g., CSV, JSON, XML).

This interface ensures that all concrete save strategy classes adhere to
a consistent method signature, making it easier to interchange
different save strategies.
"""

from abc import ABC, abstractmethod


class SaveStrategy(ABC):
    """
    Abstract base class for saving content to different file formats.

    This class defines the interface for saving content using different strategies.
    """

    @abstractmethod
    def save(self, content: str, filename: str) -> None:
        """
        Saves content to a file using a specific strategy.

        Args:
            content (str): The content to save.
            filename (str): The name of the file to save the content to.
        """
