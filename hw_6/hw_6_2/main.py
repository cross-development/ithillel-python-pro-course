"""
This module demonstrates the usage of the PageDownloader and PageSaver classes.

It:

1. Prompts the user to enter a URL.
2. Downloads the web page content using the PageDownloader.
3. Creates PageSaver instances with different save strategies (TXT, JSON, CSV, XML).
4. Saves the downloaded content to files using the respective save strategies.

This script showcases how to effectively use the provided classes
to download web pages and save them in various formats.
"""

from hw_6.hw_6_2.page_saver import PageSaver
from hw_6.hw_6_2.page_downloader import PageDownloader
from hw_6.hw_6_2.strategies.save_as_csv import SaveAsCsv
from hw_6.hw_6_2.strategies.save_as_txt import SaveAsTxt
from hw_6.hw_6_2.strategies.save_as_xml import SaveAsXml
from hw_6.hw_6_2.strategies.save_as_json import SaveAsJson

if __name__ == "__main__":
    # For instance https://www.lipsum.com
    url = input("Enter URL: ").strip()

    content = PageDownloader().download(url)

    if content:
        txt_saver = PageSaver(SaveAsTxt())
        json_saver = PageSaver(SaveAsJson())
        csv_saver = PageSaver(SaveAsCsv())
        xml_saver = PageSaver(SaveAsXml())

        txt_saver.save(content, "data/page_content.txt")
        json_saver.save(content, "data/page_content.json")
        csv_saver.save(content, "data/page_content.csv")
        xml_saver.save(content, "data/page_content.xml")
