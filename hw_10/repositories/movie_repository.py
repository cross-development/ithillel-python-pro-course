"""
Movie repository class for handling database operations.
"""

from typing import List, Dict

from hw_10.models.movie import Movie
from hw_10.database.database import Database


class MovieRepository:
    """
    Repository for movie-related operations.
    """

    def __init__(self, db: Database) -> None:
        """
        Initialize with a database instance.

        Args:
            db (Database): The database instance.
        """

        self.db = db

    def add_movie(self, movie: Movie) -> int:
        """
        Insert a new movie record.

        Args:
            movie (Movie): The movie to insert.

        Returns:
            int: ID of the inserted movie.
        """

        cursor = self.db.execute(
            "INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)",
            (movie.title, movie.release_year, movie.genre)
        )

        return cursor.lastrowid

    def add_movie_cast(self, movie_id: int, actor_id: int) -> None:
        """
        Associate an actor with a movie.

        Args:
            movie_id (int): Movie ID.
            actor_id (int): Actor ID.
        """

        self.db.execute(
            "INSERT OR IGNORE INTO movie_cast (movie_id, actor_id) VALUES (?, ?)",
            (movie_id, actor_id)
        )

    def get_movies_with_actors(self) -> List[Dict]:
        """
        Get all movies with a list of associated actors using JOIN.

        Returns:
            List[Dict]: List of movies with actor names.
        """

        query = """
            SELECT m.id, m.title, GROUP_CONCAT(a.name, ', ') AS actors
            FROM movies AS m
            INNER JOIN movie_cast AS mc ON m.id = mc.movie_id
            INNER JOIN actors AS a ON a.id = mc.actor_id
            GROUP BY m.id
        """
        rows = self.db.query(query)

        return [dict(row) for row in rows]

    def get_movies_with_age(self) -> List[Dict]:
        """
        Retrieve movies with computed age using custom function movie_age.

        Returns:
            List[Dict]: List of movies with their age.
        """

        query = "SELECT title, movie_age(release_year) AS age FROM movies"
        rows = self.db.query(query)

        return [dict(row) for row in rows]

    def get_movies_paginated(self, limit: int, offset: int) -> List[Dict]:
        """
        Retrieve movies using pagination.

        Args:
            limit (int): Number of movies per page.
            offset (int): Offset for pagination.

        Returns:
            List[Dict]: List of movies for the given page.
        """

        query = "SELECT * FROM movies LIMIT ? OFFSET ?"
        rows = self.db.query(query, (limit, offset))

        return [dict(row) for row in rows]

    def search_movies_by_title(self, keyword: str) -> List[Dict]:
        """
        Search movies by title with the LIKE operator.

        Args:
            keyword (str): Search keyword.

        Returns:
            List[Dict]: List of matching movies.
        """

        query = "SELECT * FROM movies WHERE title LIKE ?"
        keyword = f"%{keyword}%"
        rows = self.db.query(query, (keyword,))

        return [dict(row) for row in rows]

    def get_unique_genres(self) -> List[str]:
        """
        Retrieve a unique list of movie genres.

        Returns:
            List[str]: Unique genres.
        """

        query = "SELECT DISTINCT genre FROM movies"
        rows = self.db.query(query)

        return [row["genre"] for row in rows]

    def get_movie_count_by_genre(self) -> List[Dict]:
        """
        Count movies grouped by genre.

        Returns:
            List[Dict]: List of genres with counts.
        """

        query = "SELECT genre, COUNT(*) AS count FROM movies GROUP BY genre"
        rows = self.db.query(query)

        return [dict(row) for row in rows]

    def get_all_movies(self) -> List[Dict]:
        """
        Retrieve all movies.

        Returns:
            List[Dict]: All movie records.
        """

        query = "SELECT * FROM movies"
        rows = self.db.query(query)

        return [dict(row) for row in rows]
