"""
Service layer encapsulating business logic.
"""

from typing import List, Dict

from hw_10.models.movie import Movie
from hw_10.repositories.movie_repository import MovieRepository


class MovieService:
    """
    Service class for movie operations.
    """

    def __init__(self, movie_repository: MovieRepository):
        """
        Initialize the MovieService.

        Args:
            movie_repository (MovieRepository): Movie repository instance.
        """

        self.movie_repository = movie_repository

    def add_movie_with_actors(self, title: str, release_year: int, genre: str,
                              actor_ids: List[int]) -> int:
        """
        Add a movie and link it to actors.

        Args:
           title (str): Movie title.
           release_year (int): Release year.
           genre (str): Movie genre.
           actor_ids (List[int]): List of actor IDs.

        Returns:
           int: ID of the new movie.
        """

        movie = Movie(title=title, release_year=release_year, genre=genre)
        movie_id = self.movie_repository.add_movie(movie)

        for actor_id in actor_ids:
            self.movie_repository.add_movie_cast(movie_id, actor_id)

        return movie_id

    def get_movies_with_actors(self) -> List[Dict]:
        """
        Get movies along with associated actors.

        Returns:
            List[Dict]: Movies with actor details.
        """

        return self.movie_repository.get_movies_with_actors()

    def get_movies_with_age(self) -> List[Dict]:
        """
        Get movies with computed age.

        Returns:
            List[Dict]: Movies with age.
        """

        return self.movie_repository.get_movies_with_age()

    def get_movies_paginated(self, limit: int, offset: int) -> List[Dict]:
        """
        Get paginated list of movies.

        Args:
            limit (int): Page size.
            offset (int): Offset.

        Returns:
            List[Dict]: Paginated movies.
        """

        return self.movie_repository.get_movies_paginated(limit, offset)

    def search_movies_by_title(self, keyword: str) -> List[Dict]:
        """
        Search movies by title.

        Args:
            keyword (str): Search keyword.

        Returns:
            List[Dict]: Matching movies.
        """

        return self.movie_repository.search_movies_by_title(keyword)

    def get_unique_genres(self) -> List[str]:
        """
        Retrieve unique genres.

        Returns:
            List[str]: Unique genres.
        """

        return self.movie_repository.get_unique_genres()

    def get_movie_count_by_genre(self) -> List[Dict]:
        """
        Get movie counts by genre.

        Returns:
            List[Dict]: Genres with counts.
        """

        return self.movie_repository.get_movie_count_by_genre()

    def get_all_movies(self) -> List[Dict]:
        """
        Get all movies.

        Returns:
            List[Dict]: List of movies.
        """

        return self.movie_repository.get_all_movies()
