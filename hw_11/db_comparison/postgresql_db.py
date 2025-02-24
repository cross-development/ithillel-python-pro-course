"""
PostgreSQL-based To-Do list repository.
"""

import psycopg2
from typing import List, Tuple

DB_CONFIG = {
    "dbname": "todo_db",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432
}


class TodoPostgres:
    """
    A class to interact with a PostgreSQL database for managing a to-do list.

    This class provides methods for creating, reading, updating, and deleting
    tasks in a PostgreSQL database.
    """

    def __init__(self) -> None:
        """
        Initializes the PostgreSQL connection and ensures the 'tasks' table exists.

        This constructor establishes a connection to the database and creates
        the required table if it does not already exist.
        """

        self.conn = psycopg2.connect(**DB_CONFIG)
        self.cur = self.conn.cursor()
        self._ensure_table_exists()

    def _ensure_table_exists(self) -> None:
        """
        Creates the 'tasks' table if it doesn't exist.

        The table includes the following columns:
        - id: Serial primary key
        - title: Task title (required)
        - description: Task description (optional)
        - completed: Boolean flag indicating task completion (default: False)
        """

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT FALSE
            );
        """)
        self.conn.commit()

    def create_task(self, title: str, description: str) -> int:
        """
        Inserts a new task into the database and returns its ID.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.

        Returns:
            int: The ID of the inserted task.
        """

        self.cur.execute(
            "INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING id;",
            (title, description)
        )
        task_id = self.cur.fetchone()[0]
        self.conn.commit()

        return task_id

    def get_tasks(self) -> List[Tuple[int, str, str, bool]]:
        """
        Fetches all tasks from the database.

        Returns:
            List[Tuple[int, str, str, bool]]: A list of tuples, each containing:
                - task ID (int)
                - title (str)
                - description (str)
                - completion status (bool)
        """

        self.cur.execute("SELECT * FROM tasks;")

        return self.cur.fetchall()

    def update_task(self, task_id: int, title: str, description: str, completed: bool) -> None:
        """
        Updates an existing task in the database.

        Args:
            task_id (int): The ID of the task to update.
            title (str): The updated title of the task.
            description (str): The updated description of the task.
            completed (bool): The updated completion status.
        """

        self.cur.execute(
            "UPDATE tasks SET title = %s, description = %s, completed = %s WHERE id = %s;",
            (title, description, completed, task_id)
        )
        self.conn.commit()

    def delete_task(self, task_id: int) -> None:
        """
        Deletes a task from the database by its ID.

        Args:
            task_id (int): The ID of the task to delete.
        """

        self.cur.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
        self.conn.commit()

    def close(self) -> None:
        """
        Closes the database connection.
        """

        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    pg_todo = TodoPostgres()
    task_id = pg_todo.create_task("Learn Python", "Study basic syntax")

    print("Task created with ID:", task_id)
    print("All tasks:", pg_todo.get_tasks())

    pg_todo.close()
