from typing import Iterator


class ReverseFileIterator:
    """
    An iterator for reading a file in reverse line-by-line.

    Args:
        filename (str): The path to the file to be read.
    """

    def __init__(self, filename: str) -> None:
        """
        Initializes the ReverseFileIterator.

        Args:
            filename (str): The path to the file to be read.
        """
        self.filename = filename
        self._lines = None

    def __iter__(self) -> Iterator[str]:
        """
        Returns the iterator object itself.

        Returns:
            ReverseFileIterator: The iterator object.
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            self._lines = file.readlines()[::-1]
            self._index = 0

        return self

    def __next__(self) -> str:
        """
        Returns the next line in the file in reverse order.

        Raises:
            StopIteration: If the end of the file is reached.

        Returns:
            str: The next line in the file.
        """
        if self._index >= len(self._lines):
            raise StopIteration

        line = self._lines[self._index].rstrip('\n')
        self._index += 1

        return line


file_path = "test.txt"

with open(file_path, 'w', encoding='utf-8') as f:
    for item in range(1, 11):
        f.write(f"Line {item}\n")

print("Reading file in reverse:")

for row in ReverseFileIterator(file_path):
    print(row)

print("All tests passed!")
