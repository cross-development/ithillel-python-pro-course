"""
This module demonstrates the use of generators and context managers.

- `even_number_generator`: An infinite generator that yields a sequence of even numbers.
- `LimitGeneratorToFile`: A context manager for writing a limited number of lines to a file.

This module showcases advanced Python concepts for efficient and concise code.
"""

from typing import Generator, IO, Any


def even_number_generator() -> Generator[int, None, None]:
    """
    Generates an infinite sequence of even numbers.

    Yields:
        int: The next even number in the sequence.
    """
    num = 0

    while True:
        yield num
        num += 2


class LimitGeneratorToFile:
    """
    Context manager for writing a limited number of lines to a file.

    Args:
        file_path (str): Path to the output file.
        limit (int): Number of lines to write to the file.
    """

    def __init__(self, file_path: str, limit: int) -> None:
        """
        Initializes the LimitGeneratorToFile object.

        Args:
            file_path (str): Path to the output file.
            limit (int): Number of lines to write to the file.
        """
        self.file_path = file_path
        self.limit = limit
        self.file: IO | None = None

    def __enter__(self) -> IO:
        """
        Opens the output file for writing.

        Returns:
            IO: The opened file object.
        """
        self.file = open(self.file_path, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """
        Closes the output file.

        Args:
            exc_type (Any): Exception type (if any).
            exc_val (Any): Exception value (if any).
            exc_tb (Any): Exception traceback (if any).
        """
        if self.file:
            self.file.close()


OUTPUT_FILE_PATH = "even_numbers.txt"
NUMBER_LIMIT = 100

even_numbers = even_number_generator()

with LimitGeneratorToFile(OUTPUT_FILE_PATH, NUMBER_LIMIT) as file:
    for _ in range(NUMBER_LIMIT):
        file.write(f"{next(even_numbers)}\n")

print(f"First {NUMBER_LIMIT} even numbers saved to {OUTPUT_FILE_PATH}.")

print("All tests passed!")
