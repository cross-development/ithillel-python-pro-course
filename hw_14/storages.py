"""
Storage module for handling data persistence.

This module provides:
- An abstract `Storage` interface.
- A `CSVStorage` class for saving data to CSV files.
- A `CSVStorageAdapter` class to integrate CSV storage with a common interface.
"""

import csv
from typing import Dict, List
from abc import ABC, abstractmethod

from hw_14.logger import logging

logger = logging.getLogger(__name__)


class Storage(ABC):
    """
    Abstract base class for storage implementations.
    """

    @abstractmethod
    def save(self, data: List[Dict]) -> None:
        """
        Saves the provided data.

        Args:
            data (List[Dict]): A list of dictionaries representing news articles.
        """


class CSVStorage:
    """
    Handles saving news data to a CSV file.
    """

    def __init__(self, filename: str) -> None:
        """
        Initializes CSVStorage with a filename.

        Args:
            filename (str): The CSV file name where data will be stored.
        """

        self.filename = filename

    def save_to_csv(self, data: List[Dict]) -> None:
        """
        Saves the given data to a CSV file.

        Args:
            data (List[Dict]): A list of dictionaries representing news articles.
        """

        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "link", "date", "summary"])
            writer.writeheader()
            writer.writerows(data)

        logger.info(f"Saved {len(data)} records to {self.filename}")


class CSVStorageAdapter(Storage):
    """
    Adapter class to integrate CSVStorage with the Storage interface.
    """

    def __init__(self, csv_storage: CSVStorage) -> None:
        """
        Initializes CSVStorageAdapter with an instance of CSVStorage.

        Args:
            csv_storage (CSVStorage): The CSVStorage instance.
        """

        self.csv_storage = csv_storage

    def save(self, data: List[Dict]) -> None:
        """
        Saves the provided data using CSVStorage.

        Args:
            data (List[Dict]): A list of dictionaries representing news articles.
        """

        self.csv_storage.save_to_csv(data)
