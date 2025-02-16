"""
Service layer encapsulating business logic.
"""

from typing import List, Dict

from hw_10.models.actor import Actor
from hw_10.repositories.actor_repository import ActorRepository


class ActorService:
    """
    Service class for actor operations.
    """

    def __init__(self, actor_repository: ActorRepository) -> None:
        """
        Initialize the ActorService.

        Args:
            actor_repository (ActorRepository): Actor repository instance.
        """

        self.actor_repository = actor_repository

    def add_actor(self, name: str, birth_year: int) -> int:
        """
        Add a new actor.

        Args:
            name (str): Actor name.
            birth_year (int): Birth year.

        Returns:
            int: ID of the new actor.
        """

        actor = Actor(name=name, birth_year=birth_year)

        return self.actor_repository.add_actor(actor)

    def get_all_actors(self) -> List[Dict]:
        """
        Get all actors.

        Returns:
            List[Dict]: List of actor records.
        """

        return self.actor_repository.get_all_actors()

    def get_avg_birth_year_by_genre(self, genre: str) -> int:
        """
        Get average birth year of actors by movie genre.

        Args:
            genre (str): Genre filter.

        Returns:
            int: Average birth year.
        """

        return self.actor_repository.get_avg_birth_year_by_genre(genre)

    def get_all_names_union_movies(self) -> List[str]:
        """
        Retrieve union of actor names and movie titles.

        Returns:
            List[str]: Names and titles.
        """

        return self.actor_repository.get_all_names_union_movies()
