"""
Controllers layer providing an API-like interface.
"""

from typing import List, Dict

from hw_10.services.movie_service import MovieService


class MoviesController:
    """
    Controller for movie-related endpoints.
    """

    def __init__(self, movie_service: MovieService) -> None:
        """
        Initialize with a movie service.

        Args:
            movie_service (MovieService): Service instance.
        """

        self.movie_service = movie_service

    def add_movie(self, title: str, release_year: int, genre: str, actor_ids: List[int]) -> int:
        """
        Endpoint to add a movie with associated actors.

        Returns:
            int: New movie ID.
        """

        return self.movie_service.add_movie_with_actors(title, release_year, genre, actor_ids)

    def get_movies_with_actors(self) -> List[Dict]:
        """
        Endpoint to retrieve movies with actors.

        Returns:
            List[Dict]: Movies with actor details.
        """

        return self.movie_service.get_movies_with_actors()

    def get_movies_with_age(self) -> List[Dict]:
        """
        Endpoint to retrieve movies with computed age.

        Returns:
            List[Dict]: Movies with age.
        """

        return self.movie_service.get_movies_with_age()

    def get_movies_paginated(self, limit: int, offset: int) -> List[Dict]:
        """
        Endpoint to retrieve paginated movies.

        Args:
            limit (int): Page size.
            offset (int): Offset.

        Returns:
            List[Dict]: Paginated movies.
        """

        return self.movie_service.get_movies_paginated(limit, offset)

    def search_movies_by_title(self, keyword: str) -> List[Dict]:
        """
        Endpoint to search movies by title.

        Args:
            keyword (str): Search keyword.

        Returns:
            List[Dict]: Matching movies.
        """

        return self.movie_service.search_movies_by_title(keyword)

    def get_unique_genres(self) -> List[str]:
        """
        Endpoint to get unique genres.

        Returns:
            List[str]: Unique genres.
        """

        return self.movie_service.get_unique_genres()

    def get_movie_count_by_genre(self) -> List[Dict]:
        """
        Endpoint to get movie counts by genre.

        Returns:
            List[Dict]: Genres with counts.
        """

        return self.movie_service.get_movie_count_by_genre()

    def get_all_movies(self) -> List[Dict]:
        """
        Endpoint to retrieve all movies.

        Returns:
            List[Dict]: List of movies.
        """

        return self.movie_service.get_all_movies()
