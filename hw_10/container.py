"""
Dependency injection container using dependency_injector.
"""

from dependency_injector import containers, providers

from hw_10.database.database import Database
from hw_10.repositories.movie_repository import MovieRepository
from hw_10.repositories.actor_repository import ActorRepository
from hw_10.services.movie_service import MovieService
from hw_10.services.actor_service import ActorService
from hw_10.controllers.movies_controller import MoviesController
from hw_10.controllers.actors_controller import ActorsController
from hw_10.apps.console_app import ConsoleApp


class Container(containers.DeclarativeContainer):
    """
    DI container for the Cinema Database application.
    """

    config = providers.Configuration()

    # Database singleton (stores the SQLite database handling code)
    database = providers.Singleton(Database, db_path=config.db.db_path)

    # Repositories (encapsulates data access)
    movie_repository = providers.Factory(MovieRepository, db=database)
    actor_repository = providers.Factory(ActorRepository, db=database)

    # Services (contains the business logic)
    movie_service = providers.Factory(MovieService, movie_repository=movie_repository)
    actor_service = providers.Factory(ActorService, actor_repository=actor_repository)

    # Controllers (API-like layer)
    movies_controller = providers.Factory(MoviesController, movie_service=movie_service)
    actors_controller = providers.Factory(ActorsController, actor_service=actor_service)

    # Console application (host)
    console_app = providers.Factory(
        ConsoleApp,
        movies_controller=movies_controller,
        actors_controller=actors_controller)
