"""
Main entry point for the Cinema Database application.
"""

from hw_10.container import Container


def main() -> None:
    """
    Configure the dependency injection container and run the console application.
    """

    container = Container()
    container.config.db.db_path.from_value("database/cinema.db")

    app = container.console_app()
    app.run()


if __name__ == '__main__':
    main()
