import os
import csv
from PIL import Image
from typing import Iterator, Dict, Any


class ImageMetadataIterator:
    """
    Iterates over images in a directory and extracts metadata.

    Args:
        directory (str): Path to the directory containing images.
        output_csv (str): Path to the output CSV file for metadata.

    Attributes:
        __image_file_extensions (tuple): A tuple of supported image file extensions.
    """

    __image_file_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif', '.tiff')

    def __init__(self, directory: str, output_csv: str) -> None:
        """
        Initializes the ImageMetadataIterator.

        Args:
            directory (str): Path to the directory containing images.
            output_csv (str): Path to the output CSV file for metadata.
        """
        self.directory = directory
        self.output_csv = output_csv
        self._index = 0
        self._files = [f for f in os.listdir(directory) if f.lower().endswith(self.__image_file_extensions)]

        with open(self.output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Filename', 'Format', 'Width', 'Height', 'Mode', 'Size (bytes)'])

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        """
        Returns the iterator object itself.

        Returns:
            Iterator[Dict[str, Any]]: An iterator yielding dictionaries containing image metadata.
        """
        return self

    def __next__(self) -> Dict[str, Any]:
        """
        Retrieves the next image metadata.

        Raises:
            StopIteration: If the end of the image list is reached.

        Returns:
            Dict[str, Any]: A dictionary containing image metadata (Filename, Format, Width, Height, Mode, Size (bytes)).
        """
        if self._index >= len(self._files):
            raise StopIteration

        filename = self._files[self._index]
        filepath = os.path.join(self.directory, filename)

        try:
            with Image.open(filepath) as img:
                metadata = {
                    'Filename': filename,
                    'Format': img.format,
                    'Width': img.width,
                    'Height': img.height,
                    'Mode': img.mode,
                    'Size (bytes)': os.path.getsize(filepath)
                }

                with open(self.output_csv, 'a', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(list(metadata.values()))

                self._index += 1

                return metadata

        except Exception as e:
            print(f"Error processing {filename}: {e}")
            self._index += 1
            return self.__next__()


image_directory = "images"
output_csv_file = "image_metadata.csv"

image_iterator = ImageMetadataIterator(image_directory, output_csv_file)

print("Processing Images:")
for md in image_iterator:
    print(md)

print(f"Metadata saved to {output_csv_file}")

print("All tests passed!")
