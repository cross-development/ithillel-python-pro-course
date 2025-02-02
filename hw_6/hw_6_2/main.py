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
