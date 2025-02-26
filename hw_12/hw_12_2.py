"""
Multi-threaded Image Resizer.

This module resizes multiple images concurrently using ThreadPoolExecutor.
"""

import os
from PIL import Image
from typing import Tuple, List
from concurrent.futures import ThreadPoolExecutor


def resize_image(image_path: str, output_path: str, size: Tuple[int, int] = (128, 128)) -> None:
    """
    Resizes an image to the specified dimensions and saves it.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the resized image.
        size (Tuple[int, int], optional): Target size (width, height). Defaults to (128, 128).

    Raises:
        IOError: If the image cannot be opened or saved.
    """

    try:
        with Image.open(image_path) as img:
            img = img.resize(size, Image.Resampling.LANCZOS)
            img.save(output_path)

            print(f"Resized and saved: {output_path}")
    except IOError as e:
        print(f"Failed to process {image_path}: {e}")


def resize_images_concurrently(image_paths: List[str], output_paths: List[str],
                               size: Tuple[int, int] = (128, 128)) -> None:
    """
    Resizes multiple images concurrently using a thread pool.

    Args:
        image_paths (List[str]): List of input image paths.
        output_paths (List[str]): List of output image paths.
        size (Tuple[int, int], optional): Target size (width, height). Defaults to (128, 128).
    """

    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as executor:
        for image_path, output_path in zip(image_paths, output_paths):
            executor.submit(resize_image, image_path, output_path, size)

    print("✅ All images processed.")


if __name__ == "__main__":
    image_paths = [
        "images/image_1.jpg",
        "images/image_2.jpg",
        "images/image_3.jpg"
    ]
    output_paths = [
        "images/resized/resized_1.jpg",
        "images/resized/resized_2.jpg",
        "images/resized/resized_3.jpg"
    ]

    resize_images_concurrently(image_paths, output_paths)
