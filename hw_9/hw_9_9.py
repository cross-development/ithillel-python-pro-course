"""
Module for analyzing a web server log file and extracting request statistics.
"""

import re
from typing import Dict
from collections import Counter


def analyze_log_file(file_path: str) -> Dict[str, int]:
    """
    Reads a web server log file and counts requests from different IP addresses.

    Args:
        file_path (str): Path to the log file.

    Returns:
        Dict[str, int]: A dictionary mapping IP addresses to the number of requests.
    """

    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ip_counter = Counter()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                match = re.search(ip_pattern, line)

                if match:
                    ip_counter[match.group()] += 1
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}

    return dict(ip_counter)


if __name__ == "__main__":
    LOG_FILE = "web_server.log"
    statistics = analyze_log_file(LOG_FILE)

    if statistics:
        print("IP Address Request Count:")

        for ip, count in statistics.items():
            print(f"{ip}: {count}")
