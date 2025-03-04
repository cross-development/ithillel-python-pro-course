"""
Request Configuration Constants.
This module defines configuration constants for handling HTTP requests.
"""

# Total number of requests to be processed
NUMBER_OF_REQUESTS = 500

# Timeout settings for HTTP requests
LONG_REQUEST_TIMEOUT = 10  # Timeout for long-running requests (in seconds)
SHORT_REQUEST_TIMEOUT = 5  # Timeout for short requests (in seconds)

# Maximum number of concurrent requests
CONCURRENT_REQUEST_LIMIT = 2

# Maximum number of concurrent requests to download web page
CONCURRENT_DOWNLOAD_LIMIT = 3
