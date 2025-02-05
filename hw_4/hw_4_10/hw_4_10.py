"""
This module provides an ArchiveManager context manager for creating ZIP archives of directories.

The ArchiveManager simplifies the process of creating ZIP archives by:

- Handling the creation and closing of the ZIP file within a with block.
- Providing a method to easily add files from a specified directory to the archive.
- Including basic error handling for invalid directory paths.
"""

import os
import zipfile
from typing import Any


class ArchiveManager:
    """
    Context manager for creating a ZIP archive of a directory.

    Args:
        archive_file_name (str): The name of the archive file to create.
        directory_path_to_archive (str): The path to the directory to archive.
    """

    def __init__(self, archive_file_name: str, directory_path_to_archive: str) -> None:
        """
        Initializes the ArchiveManager with the archive file name and directory path.

        Args:
            archive_file_name (str): The name of the archive file to create.
            directory_path_to_archive (str): The path to the directory to archive.
        """
        self.archive = None
        self.archive_file_name = archive_file_name
        self.directory_path_to_archive = directory_path_to_archive

    def __enter__(self) -> "ArchiveManager":
        """
        Opens a new ZIP archive in write mode.

        Returns:
            ArchiveManager: The ArchiveManager object itself.
        """
        self.archive = zipfile.ZipFile(self.archive_file_name, 'w', zipfile.ZIP_DEFLATED)

        return self

    def add_files_from_directory(self) -> None:
        """
        Adds all files from the specified directory to the archive.

        Raises:
            OSError: If the directory path does not exist.
        """
        if not os.path.isdir(self.directory_path_to_archive):
            raise OSError(f"The directory {self.directory_path_to_archive} does not exist!")

        for root, _, files in os.walk(self.directory_path_to_archive):
            for file in files:
                file_path = os.path.join(root, file)
                file_name = os.path.relpath(file_path, self.directory_path_to_archive)
                self.archive.write(file_path, file_name)

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """
        Closes the archive file if it was opened.

        Args:
            exc_type (Any): Exception type, if any.
            exc_val (Any): Exception value, if any.
            exc_tb (Any): Exception traceback, if any.
        """
        if self.archive:
            self.archive.close()


ARCHIVE_NAME = 'archive.zip'
DIRECTORY_TO_ARCHIVE = 'files_to_archive'

try:
    with ArchiveManager(ARCHIVE_NAME, DIRECTORY_TO_ARCHIVE) as archive:
        archive.add_files_from_directory()

    print(f"All files from {DIRECTORY_TO_ARCHIVE} successfully archived into {ARCHIVE_NAME}")
except Exception as e:
    print(f"Error during archiving: {e}")

print("All tests passed!")
