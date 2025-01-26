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


output_file_path = "even_numbers.txt"
number_limit = 100

even_numbers = even_number_generator()

with LimitGeneratorToFile(output_file_path, number_limit) as file:
    for _ in range(number_limit):
        file.write(f"{next(even_numbers)}\n")

print(f"First {number_limit} even numbers saved to {output_file_path}.")

print("All tests passed!")
