"""
Database module for handling SQLite operations.
"""

import sqlite3
import datetime
from typing import List, Any, Tuple


class Database:
    """
    Database class to encapsulate SQLite operations and custom functions.
    """

    def __init__(self, db_path: str = "cinema.db") -> None:
        """
        Initialize the database connection and create tables.

        Args:
            db_path (str): Path to the SQLite database file.
        """

        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self._register_functions()
        self._create_tables()

    def _register_functions(self) -> None:
        """
        Register custom SQLite functions.
        """

        def movie_age(release_year: int) -> int:
            """
            Calculate the number of years since the movie was released.

            Args:
                release_year (int): The movie's release year.

            Returns:
                int: Years elapsed since release.
            """

            current_year = datetime.datetime.now().year

            return current_year - release_year

        self.connection.create_function("movie_age", 1, movie_age)

    def _create_tables(self):
        """
        Create tables for movies, actors, and movie_cast if they do not exist.
        """

        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY,
                title TEXT,
                release_year INTEGER,
                genre TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY,
                name TEXT,
                birth_year INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movie_cast (
                movie_id INTEGER,
                actor_id INTEGER,
                PRIMARY KEY(movie_id, actor_id),
                FOREIGN KEY(movie_id) REFERENCES movies(id),
                FOREIGN KEY(actor_id) REFERENCES actors(id)
            )
        """)

        self.connection.commit()

    def execute(self, query: str, params: Tuple[Any] = ()) -> sqlite3.Cursor:
        """
        Execute an SQL query with parameters.

        Args:
            query (str): The SQL query.
            params (Tuple[Any]): Query parameters.

        Returns:
            sqlite3.Cursor: Cursor after execution.
        """

        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()

        return cursor

    def query(self, query: str, params: Tuple[Any] = ()) -> List[sqlite3.Row]:
        """
        Execute an SQL query and return all rows.

        Args:
            query (str): The SQL query.
            params (Tuple[Any]): Query parameters.

        Returns:
            List[sqlite3.Row]: Query result rows.
        """

        cursor = self.connection.cursor()
        cursor.execute(query, params)

        return cursor.fetchall()

    def close(self) -> None:
        """
        Close the database connection.
        """

        self.connection.close()
