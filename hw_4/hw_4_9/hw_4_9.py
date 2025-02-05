"""
This module provides a BackupManager context manager for creating backups of files
before processing and restoring them in case of errors.

The BackupManager creates a backup of the specified file before entering the `with` block.
If an exception occurs within the `with` block, the BackupManager restores the original
file from the backup. This ensures data integrity and allows for easy recovery in case of issues.
"""

import os
import shutil
from typing import Any


class BackupManager:
    """
    Context manager for creating a backup of a file before processing and restoring it on failure.

    Args:
        file_path (str): Path to the file to be backed up.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initializes the BackupManager with the file path.

        Args:
            file_path (str): Path to the file to be backed up.
        """
        self.file_path = file_path
        self.backup_file = file_path + ".bak"

    def __enter__(self) -> None:
        """
        Creates a backup of the file before entering the with block.
        """
        shutil.copy2(self.file_path, self.backup_file)

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        """
        Handles exit from the with block.

        Args:
            exc_type (Any): Exception type, if any.
            exc_val (Any): Exception value, if any.
            exc_tb (Any): Exception traceback, if any.

        Returns:
            bool: True if the exception was handled, False otherwise.
        """
        if exc_type is None:
            # Successful execution, delete the backup
            os.remove(self.backup_file)
        else:
            # An error occurred, restore the original file from backup, and remove backup
            shutil.copy2(self.backup_file, self.file_path)
            os.remove(self.backup_file)

        return True


FILE_TO_PROCESS = 'important_file.txt'

try:
    with BackupManager(FILE_TO_PROCESS) as manager:
        with open(FILE_TO_PROCESS, 'w', encoding='utf-8') as f:
            f.write("This is the updated content.")

        print("File processed successfully.")
except Exception as e:
    print(f"Error while processing the file: {e}")

print("All tests passed!")
