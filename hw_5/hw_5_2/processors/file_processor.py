from typing import List, Union
from abc import ABC, abstractmethod


class FileProcessor(ABC):
    """
    Abstract base class for processing files.

    Args:
        filename (str): The path to the file.
    """

    def __init__(self, filename: str) -> None:
        """
        Initializes the FileProcessor.

        Args:
            filename (str): The path to the file.
        """
        self.filename = filename

    def process(self) -> Union[float, None]:
        """
        Processes the file and returns the result.

        Returns:
            Union[float, None]: The result of the processing, or None if an error occurs.
        """
        try:
            lines = self._read_file()
            numbers = self._extract_numbers(lines)

            return self._calculate(numbers)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: The file contains no valid numbers to calculate an average.")

        return None

    def _read_file(self) -> List[str]:
        """
        Reads the file and returns its lines.

        Returns:
            List[str]: A list of strings, where each string is a line from the file.
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.readlines()

    @abstractmethod
    def _extract_numbers(self, lines: List[str]) -> List[float]:
        """
        Extracts numbers from the lines read from the file.

        Args:
            lines (List[str]): A list of strings, where each string is a line from the file.

        Returns:
            List[float]: A list of floating-point numbers extracted from the lines.
        """
        pass

    @abstractmethod
    def _calculate(self, numbers: List[float]) -> float:
        """
        Calculates a value based on the extracted numbers.

        Args:
            numbers (List[float]): A list of floating-point numbers.

        Returns:
            float: The calculated value.
        """
        pass
