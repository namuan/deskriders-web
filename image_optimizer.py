#!/usr/bin/env python3

"""
Image Optimizer for Non-Committed Files in a Specific Directory

This script optimizes non-committed image files in a specified directory within a Git repository.
It reports the total file size difference after optimization.

Usage:
    python image_optimizer.py --path /path/to/images/directory [-v] [-vv]

Arguments:
    --path  : Path to the images directory (relative to the Git repository root)
    -v      : Enable verbose logging
    -vv     : Enable very verbose logging

Example:
    python image_optimizer.py --path static/images -v

Required packages:
    pip install pillow gitpython
"""

import os
import argparse
import logging
from PIL import Image
from git import Repo
from git.exc import InvalidGitRepositoryError
from argparse import ArgumentParser, RawDescriptionHelpFormatter


def setup_logging(verbose_level):
    log_levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    logging.basicConfig(level=log_levels[min(verbose_level, 2)],
                        format='%(asctime)s - %(levelname)s - %(message)s')


def parse_arguments():
    parser = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("--path", required=True,
                        help="Path to the images directory (relative to the Git repository root)")
    parser.add_argument("-v", action="count", default=0, help="Increase verbosity")
    return parser.parse_args()


def is_image_file(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))


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


def get_non_committed_images(repo, images_path):
    try:
        non_committed_files = [item.a_path for item in repo.index.diff(None)]
        non_committed_files.extend(repo.untracked_files)
        return [f for f in non_committed_files
                if f.startswith(images_path) and is_image_file(f)]
    except InvalidGitRepositoryError:
        logging.error("The current directory is not a valid Git repository.")
        return []


def process_non_committed_images(repo, images_path):
    total_size_difference = 0
    non_committed_images = get_non_committed_images(repo, images_path)
    for image_path in non_committed_images:
        full_path = os.path.join(repo.working_dir, image_path)
        total_size_difference += optimize_image(full_path)
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

    try:
        repo = Repo(os.getcwd())
    except InvalidGitRepositoryError:
        logging.error("The current directory is not a valid Git repository.")
        return

    images_path = args.path.rstrip(os.sep)
    if not os.path.isdir(images_path):
        logging.error(f"The path {images_path} is not a valid directory.")
        return

    logging.info(f"Starting image optimization for non-committed files in {images_path}")
    total_size_difference = process_non_committed_images(repo, images_path)
    logging.info("Image optimization completed")

    formatted_size_difference = format_size(total_size_difference)
    print(f"Total file size reduction: {formatted_size_difference}")


if __name__ == "__main__":
    main()
