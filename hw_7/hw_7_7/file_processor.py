"""
This module provides a FileProcessor class with static methods for file I/O operations.

- `write_to_file(file_path, data)`: Writes the given data to the specified file.
- `read_from_file(file_path)`: Reads the contents of the specified file and returns them as a string
    Raises a FileNotFoundError if the file does not exist.
"""


class FileProcessor:
    """
    A utility class for performing file I/O operations.
    """

    @staticmethod
    def write_to_file(file_path: str, data: str) -> None:
        """
        Writes the given data to the specified file.

        Args:
            file_path (str): The path to the file.
            data (str): The data to be written to the file.
        """

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Reads the contents of the specified file and returns them as a string.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The contents of the file as a string.

        Raises:
            FileNotFoundError: If the file does not exist.
        """

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found")
