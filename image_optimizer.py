#!/usr/bin/env python3

"""
Image Optimizer

This script optimizes all images in a given directory and its subdirectories for web use.
It also reports the total file size difference after optimization.

Usage:
    python image_optimizer.py --path /path/to/images/directory [-v] [-vv]

Arguments:
    --path  : Path to the directory containing images
    -v      : Enable verbose logging
    -vv     : Enable very verbose logging

Example:
    python image_optimizer.py --path /Users/nnn/workspace/deskriders-web/static -v

Required packages:
    pip install pillow
"""

import os
import argparse
import logging
from PIL import Image


def setup_logging(verbose_level):
    log_levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    logging.basicConfig(level=log_levels[min(verbose_level, 2)],
                        format='%(asctime)s - %(levelname)s - %(message)s')


def parse_arguments():
    parser = argparse.ArgumentParser(description="Optimize images for web use")
    parser.add_argument("--path", required=True, help="Path to the directory containing images")
    parser.add_argument("-v", action="count", default=0, help="Increase verbosity")
    return parser.parse_args()


def is_image_file(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))


def get_file_size(file_path):
    return os.path.getsize(file_path)


def optimize_image(file_path):
    try:
        original_size = get_file_size(file_path)
        with Image.open(file_path) as img:
            img.save(file_path, optimize=True, quality=85)
        new_size = get_file_size(file_path)
        size_difference = original_size - new_size
        logging.info(f"Optimized: {file_path} (Saved {size_difference} bytes)")
        return size_difference
    except Exception as e:
        logging.error(f"Error optimizing {file_path}: {str(e)}")
        return 0


def process_directory(directory_path):
    total_size_difference = 0
    for root, _, files in os.walk(directory_path):
        for file in files:
            if is_image_file(file):
                file_path = os.path.join(root, file)
                total_size_difference += optimize_image(file_path)
    return total_size_difference


def format_size(size_in_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} TB"


def main():
    args = parse_arguments()
    setup_logging(args.v)

    logging.info(f"Starting image optimization in: {args.path}")
    total_size_difference = process_directory(args.path)
    logging.info("Image optimization completed")

    formatted_size_difference = format_size(total_size_difference)
    print(f"Total file size reduction: {formatted_size_difference}")


if __name__ == "__main__":
    main()
