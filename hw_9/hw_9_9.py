"""
Module for analyzing a web server log file and extracting request statistics.
"""

import re
from typing import Dict
from collections import Counter


def analyze_log(log_content: str) -> Dict[str, int]:
    """
    Analyzes a web server log and counts requests per IP address.

    Args:
        log_content (str): The content of the log file.

    Returns:
        Dict[str, int]: A dictionary with IP addresses as keys and request counts as values.
    """

    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ip_addresses = re.findall(pattern, log_content)

    return dict(Counter(ip_addresses))


if __name__ == "__main__":
    SAMPLE_LOG = "192.168.0.1 - GET /index.html\n \
                  192.168.0.1 - GET /about.html\n \
                  180.151.0.2 - POST /login\n"

    print(analyze_log(SAMPLE_LOG))
