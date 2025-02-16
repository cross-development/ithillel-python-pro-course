"""
Console application acting as a host.
"""

from hw_10.controllers.movies_controller import MoviesController
from hw_10.controllers.actors_controller import ActorsController


class ConsoleApp:
    """
    Console application for user interaction.
    """

    def __init__(self, movies_controller: MoviesController,
                 actors_controller: ActorsController) -> None:
        """
        Initialize with controllers.

        Args:
            movies_controller (MoviesController): Controller for movie endpoints.
            actors_controller (ActorsController): Controller for actor endpoints.
        """

        self.movies_controller = movies_controller
        self.actors_controller = actors_controller

    def run(self) -> None:
        """
        Main loop for console application.
        """

        while True:
            self.print_menu()

            try:
                choice = int(input("Select an action: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            except KeyboardInterrupt:
                return print("\nBye!")

            if choice == 1:
                self.add_movie()
            elif choice == 2:
                self.add_actor()
            elif choice == 3:
                self.show_movies_with_actors()
            elif choice == 4:
                self.show_unique_genres()
            elif choice == 5:
                self.show_movie_count_by_genre()
            elif choice == 6:
                self.show_avg_birth_year_by_genre()
            elif choice == 7:
                self.search_movie_by_title()
            elif choice == 8:
                self.show_movies_paginated()
            elif choice == 9:
                self.show_union_actors_movies()
            elif choice == 10:
                self.show_movies_with_age()
            elif choice == 0:
                return self.stop()
            else:
                print("Invalid option. Please try again.")

    def stop(self) -> None:
        """
        Stop process and close a database connection.
        """

        print("Exiting application...")

        self.movies_controller.movie_service.movie_repository.db.close()


    def print_menu(self) -> None:
        """
        Print the main menu.
        """

        print("\nMenu:")
        print("1. Add movie")
        print("2. Add actor")
        print("3. Show all movies with actors")
        print("4. Show unique genres")
        print("5. Show movie count by genre")
        print("6. Show average birth year of actors in movies by genre")
        print("7. Search movie by title")
        print("8. Show movies (paginated)")
        print("9. Show union of actor names and movie titles")
        print("10. Show movies with their age")
        print("0. Exit\n")

    def add_movie(self) -> None:
        """
        Handle adding a new movie. Before collecting movie details,
        check if at least one actor exists; if not, inform the user.
        """

        # Check if any actors exist
        actors = self.actors_controller.get_all_actors()

        if not actors:
            return print("No actors found. Please add an actor before creating a movie.")

        # Asking for movie details first
        title = input("Enter movie title: ")

        try:
            release_year = int(input("Enter release year: "))
        except ValueError:
            return print("Invalid release year.")

        genre = input("Enter genre: ")

        actors = self.actors_controller.get_all_actors()
        # Sort actors alphabetically by name
        actors_sorted = sorted(actors, key=lambda a: a["name"])

        print("Available actors:")
        for idx, actor in enumerate(actors_sorted, start=1):
            print(f"{idx}. {actor['name']} - Birth Year: {actor['birth_year']}")

        # Asking the user to select actors by entering space-separated numbers
        selected_indices_str = input("Select actors by entering numbers separated by space: ")

        try:
            selected_indices = [int(x) for x in selected_indices_str.split() if x.strip()]
        except ValueError:
            return print("Invalid input for selection.")

        # Map selected indices to actor IDs
        actor_ids = []

        for index in selected_indices:
            if 1 <= index <= len(actors_sorted):
                actor_ids.append(actors_sorted[index - 1]["id"])
            else:
                print(f"Index {index} is out of range. Skipping.")

        if not actor_ids:
            return print("No valid actors selected. Aborting movie creation...")

        movie_id = self.movies_controller.add_movie(title, release_year, genre, actor_ids)

        print(f"Movie added with ID: {movie_id}")

    def add_actor(self) -> None:
        """
        Handle adding a new actor.
        """

        name = input("Enter actor name: ")

        try:
            birth_year = int(input("Enter birth year: "))
        except ValueError:
            return print("Invalid birth year.")

        actor_id = self.actors_controller.add_actor(name, birth_year)

        print(f"Actor added with ID: {actor_id}")

    def show_movies_with_actors(self) -> None:
        """
        Display movies along with their associated actors.
        """

        movies = self.movies_controller.get_movies_with_actors()

        print("Movies and actors:")

        if movies:
            for movie in movies:
                print(f"{movie['id']}. Movie: \"{movie['title']}\", Actors: {movie['actors']}")
        else:
            return print("No movies found.")

    def show_unique_genres(self) -> None:
        """
        Display a list of unique movie genres.
        """

        genres = self.movies_controller.get_unique_genres()

        print("Unique genres:")

        if genres:
            for idx, genre in enumerate(genres, start=1):
                print(f"{idx}. {genre}")
        else:
            return print("No genres found.")

    def show_movie_count_by_genre(self) -> None:
        """
        Display the count of movies for each genre.
        """

        counts = self.movies_controller.get_movie_count_by_genre()

        print("Movie count by genre:")

        if counts:
            for idx, entry in enumerate(counts, start=1):
                print(f"{idx}. {entry['genre']}: {entry['count']}")
        else:
            return print("No movies found.")

    def show_avg_birth_year_by_genre(self) -> None:
        """
        Display the average birth year of actors for movies in a specific genre.
        """

        genre = input("Enter genre: ")
        avg_birth_year = self.actors_controller.get_avg_birth_year_by_genre(genre)

        print(f"Average birth year of actors in {genre} movies: {avg_birth_year}")

    def search_movie_by_title(self) -> None:
        """
        Search for movies by title using a keyword.
        """

        keyword = input("Enter keyword for search: ")
        movies = self.movies_controller.search_movies_by_title(keyword)

        print("Movies by the keyword:")

        if movies:
            for movie in movies:
                print(f"{movie['id']}. {movie['title']} ({movie['release_year']})")
        else:
            print("No movies found.")

    def show_movies_paginated(self) -> None:
        """
        Display movies using pagination.
        """

        try:
            limit = int(input("Enter number of movies per page: "))
        except ValueError:
            return print("Invalid number.")

        all_movies = self.movies_controller.get_all_movies()
        total_movies = len(all_movies)
        pages = (total_movies + limit - 1) // limit
        current_page = 0

        while True:
            offset = current_page * limit
            movies = self.movies_controller.get_movies_paginated(limit, offset)

            if not movies:
                print("No more movies.")
                break

            print(f"Page {current_page + 1} of {pages}:")
            for movie in movies:
                print(f"{movie['id']}. {movie['title']}")

            nav = input("Enter 'n' for next page, 'p' for previous page, 'q' to quit pagination: ")

            if nav.lower() == 'n':
                if current_page < pages - 1:
                    current_page += 1
                else:
                    print("This is the last page.")
            elif nav.lower() == 'p':
                if current_page > 0:
                    current_page -= 1
                else:
                    print("This is the first page.")
            elif nav.lower() == 'q':
                break
            else:
                print("Invalid input.")

    def show_union_actors_movies(self) -> None:
        """
        Display a union of actor names and movie titles.
        """

        names = self.actors_controller.get_all_names_union_movies()

        print("Union of actor names and movie titles:")

        if names:
            for idx, name in enumerate(names, start=1):
                print(f"{idx}. {name}")
        else:
            return print("No actors and movies found.")

    def show_movies_with_age(self) -> None:
        """
        Display movies along with their computed age (using the movie_age custom function).
        """

        movies = self.movies_controller.get_movies_with_age()

        print("Movies and their age:")

        if movies:
            for idx, movie in enumerate(movies, start=1):
                print(f"{idx}. Movie: \"{movie['title']}\" — {movie['age']} years")
        else:
            return print("No movies found.")
