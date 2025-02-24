"""
MongoDB Backup Service.

This module provides functionality to create and manage backups of a MongoDB database.
"""

import os
import subprocess
import datetime
import shutil


class MongoBackupService:
    """
    A service for creating and managing MongoDB backups.

    This class allows creating backups of a MongoDB database and automatically
    removes older backups to retain only the latest ones.
    """

    def __init__(self, db_name: str, backup_dir: str, keep_last_n: int = 5) -> None:
        """
        Initializes the MongoBackupService.

        This constructor ensures that the backup directory exists.

        Args:
            db_name (str): The name of the MongoDB database.
            backup_dir (str): The directory to store backups.
            keep_last_n (int, optional): The number of latest backups to keep. Defaults to 5.
        """

        self.db_name = db_name
        self.backup_dir = backup_dir
        self.keep_last_n = keep_last_n
        os.makedirs(self.backup_dir, exist_ok=True)

    def create_backup(self) -> str:
        """
        Creates a backup of the MongoDB database.

        The backup is stored in the specified directory with a timestamped folder name.
        Older backups are automatically cleaned up after a successful backup.

        Returns:
            str: The path to the created backup directory, or an empty string if the backup fails.
        """

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_path = os.path.join(self.backup_dir, f"backup_{timestamp}")

        try:
            subprocess.run(["mongodump", "--db", self.db_name, "--out", backup_path], check=True)
            print(f"Backup created: {backup_path}")
            self._cleanup_old_backups()

            return backup_path
        except subprocess.CalledProcessError as e:
            print(f"Backup failed: {e}")
            return ""

    def _cleanup_old_backups(self) -> None:
        """
        Removes older backups, keeping only the latest N copies.

        This method scans the backup directory, sorts backups by modification time,
        and deletes the oldest ones if the number of backups exceeds the retention limit.
        """

        backups = sorted(
            [d for d in os.listdir(self.backup_dir) if d.startswith("backup_")],
            key=lambda d: os.path.getmtime(os.path.join(self.backup_dir, d)),
            reverse=True
        )

        for old_backup in backups[self.keep_last_n:]:
            old_backup_path = os.path.join(self.backup_dir, old_backup)
            shutil.rmtree(old_backup_path)
            print(f"Deleted old backup: {old_backup_path}")


if __name__ == "__main__":
    backup_service = MongoBackupService(db_name="online_store", backup_dir="./mongo_backups")
    backup_service.create_backup()
