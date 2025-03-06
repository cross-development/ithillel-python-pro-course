"""
Main entry point for the news processing system.

This script initializes all required components, configures them, and runs the
news extraction, filtering, and storage process.
"""

from hw_14.config import Config
from hw_14.logger import logging
from hw_14.news_service import NewsService
from hw_14.parsers import NewsParserFactory
from hw_14.filters import DateFilterStrategy
from hw_14.fetchers import RequestsPageFetcher
from hw_14.storages import CSVStorage, CSVStorageAdapter

logger = logging.getLogger(__name__)


def main() -> None:
    """
    Main function to orchestrate the news fetching, parsing, filtering, and storage process.

    - Loads configuration settings.
    - Initializes necessary components (fetcher, parser, filter, storage).
    - Creates a `NewsService` instance to process news.
    - Logs the process and executes the news processing workflow.
    """

    # Load configuration settings
    config = Config()

    # Initialize components
    fetcher = RequestsPageFetcher()
    parser_factory = NewsParserFactory.create_parser(config.site_name)
    filter_strategy = DateFilterStrategy(days=config.days_to_filter)
    csv_storage = CSVStorage(filename='news.csv')
    storage = CSVStorageAdapter(csv_storage)

    # Create and execute the news processing service
    news_service = NewsService(fetcher, parser_factory, filter_strategy, storage)

    logger.info(f"Parsing news from {config.base_url}")
    news_service.process_news(config.base_url)


if __name__ == "__main__":
    main()
