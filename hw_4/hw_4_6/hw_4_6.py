import os
from typing import Iterator, Tuple


class DirectoryFileIterator:
    """
    Iterates over files in a given directory and yields their names and sizes.

    Args:
        directory_path (str): Path to the directory to iterate over.

    Raises:
        ValueError: If the provided path is not a valid directory.
    """

    def __init__(self, directory_path: str) -> None:
        """
        Initializes the DirectoryFileIterator.

        Args:
            directory_path (str): Path to the directory to iterate over.

        Raises:
            ValueError: If the provided path is not a valid directory.
        """
        if not os.path.isdir(directory_path):
            raise ValueError(f'The path "{directory_path}" is not a valid directory')

        self.directory_path = directory_path
        self.files = iter(os.listdir(directory_path))

    def __iter__(self) -> Iterator[Tuple[str, int]]:
        """
        Returns the iterator object itself.

        Returns:
            Iterator[Tuple[str, int]]: An iterator yielding tuples of (filename, file_size).
        """
        return self

    def __next__(self) -> Tuple[str, int]:
        """
        Retrieves the next file name and its size.

        Returns:
            Tuple[str, int]: A tuple containing the filename and its size in bytes.
        """
        while True:
            file_name = next(self.files)
            file_path = os.path.join(self.directory_path, file_name)

            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)

                return file_name, file_size


directory = "file_dir"

try:
    file_iterator = DirectoryFileIterator(directory)

    for name, size in file_iterator:
        print(f"File: {name}, Size: {size} bytes")
except ValueError as e:
    print(e)

print("All tests passed!")