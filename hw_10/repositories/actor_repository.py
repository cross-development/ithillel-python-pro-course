"""
Actor repository class for handling database operations.
"""

from typing import List, Dict

from hw_10.models.actor import Actor
from hw_10.database.database import Database


class ActorRepository:
    """
    Repository for actor-related operations.
    """

    def __init__(self, db: Database) -> None:
        """
        Initialize with a database instance.

        Args:
            db (Database): The database instance.
        """

        self.db = db

    def add_actor(self, actor: Actor) -> int:
        """
        Insert a new actor record.

        Args:
            actor (Actor): The actor to insert.

        Returns:
            int: ID of the inserted actor.
        """

        cursor = self.db.execute(
            "INSERT INTO actors (name, birth_year) VALUES (?, ?)",
            (actor.name, actor.birth_year),
        )

        return cursor.lastrowid

    def get_all_actors(self) -> List[Dict]:
        """
        Retrieve all actor records.

        Returns:
            List[Dict]: List of all actors.
        """

        query = "SELECT * FROM actors"
        rows = self.db.query(query)

        return [dict(row) for row in rows]

    def get_avg_birth_year_by_genre(self, genre: str) -> int:
        """
        Calculate the average birth year of actors in a specific genre.

        Args:
            genre (str): Genre filter.

        Returns:
            int: Average birth year.
        """

        query = """
            SELECT AVG(a.birth_year) AS avg_birth_year
            FROM actors AS a
            INNER JOIN movie_cast AS mc ON a.id = mc.actor_id
            INNER JOIN movies AS m ON m.id = mc.movie_id
            WHERE m.genre = ?
        """
        rows = self.db.query(query, (genre,))

        return round(rows[0]["avg_birth_year"]) \
            if rows and rows[0]["avg_birth_year"] is not None else 0

    def get_all_names_union_movies(self) -> List[str]:
        """
        Retrieve a union of actor names and movie titles.

        Returns:
            List[str]: List of names.
        """

        query = """
            SELECT name FROM actors
            UNION
            SELECT title FROM movies
        """
        rows = self.db.query(query)

        return [list(row)[0] for row in rows]
