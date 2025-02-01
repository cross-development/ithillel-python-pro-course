from hw_6.hw_6_2.strategies.save_strategy import SaveStrategy


class PageSaver:
    """
    Class for saving downloaded web page content using different strategies.
    """

    def __init__(self, strategy: SaveStrategy) -> None:
        """
        Initializes the PageSaver with a given save strategy.

        Args:
            strategy (SaveStrategy): The initial save strategy to use.
        """

        self.strategy = strategy

    def set_strategy(self, strategy: SaveStrategy) -> None:
        """
        Sets a new save strategy.

        Args:
            strategy (SaveStrategy): The new save strategy to use.
        """

        self.strategy = strategy

    def save(self, content: str, filename: str) -> None:
        """
        Saves the given content using the current save strategy.

        Args:
            content (str): The content to save.
            filename (str): The name of the file to save the content to.
        """

        self.strategy.save(content, filename)
