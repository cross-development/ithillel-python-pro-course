"""
Controllers layer providing an API-like interface.
"""

from typing import List, Dict

from hw_10.services.actor_service import ActorService


class ActorsController:
    """
    Controller for actor-related endpoints.
    """

    def __init__(self, actor_service: ActorService) -> None:
        """
        Initialize with an actor service.

        Args:
            actor_service (ActorService): Service instance.
        """

        self.actor_service = actor_service

    def add_actor(self, name: str, birth_year: int) -> int:
        """
        Endpoint to add a new actor.

        Args:
            name (str): Actor name.
            birth_year (int): Birth year.

        Returns:
            int: New actor ID.
        """

        return self.actor_service.add_actor(name, birth_year)

    def get_all_actors(self) -> List[Dict]:
        """
        Controller endpoint to retrieve all actors.

        Returns:
            List[Dict]: List of actors.
        """

        return self.actor_service.get_all_actors()

    def get_avg_birth_year_by_genre(self, genre: str) -> int:
        """
        Endpoint to get average birth year for a genre.

        Args:
            genre (str): Genre filter.

        Returns:
            int: Average birth year.
        """

        return self.actor_service.get_avg_birth_year_by_genre(genre)

    def get_all_names_union_movies(self) -> List[str]:
        """
        Endpoint to get a union of actor names and movie titles.

        Returns:
            List[str]: Names and titles.
        """

        return self.actor_service.get_all_names_union_movies()
