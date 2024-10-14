#!/usr/bin/env python3
"""
A script to process blog post images.

Usage:
./process_blog_images.py -h

./process_blog_images.py -v path/to/blog_post.md # To log INFO messages
./process_blog_images.py -vv path/to/blog_post.md # To log DEBUG messages
"""
import logging
import os
import re
import shutil
import time
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from datetime import datetime


def setup_logging(verbosity):
    logging_level = logging.WARNING
    if verbosity == 1:
        logging_level = logging.INFO
    elif verbosity >= 2:
        logging_level = logging.DEBUG

    logging.basicConfig(
        handlers=[
            logging.StreamHandler(),
        ],
        format="%(asctime)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging_level,
    )
    logging.captureWarnings(capture=True)


def parse_args():
    parser = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument(
        "blog_post",
        help="Relative path to the blog post file",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        dest="verbose",
        help="Increase verbosity of logging output",
    )
    return parser.parse_args()


def generate_target_location():
    now = datetime.now()
    timestamp = int(time.time())
    return f"images/{now.year}/{now.month:02d}/{now.day:02d}/{timestamp}.png"


def process_blog_post(blog_post_path):
    logging.info(f"Processing blog post: {blog_post_path}")

    with open(blog_post_path, 'r') as file:
        content = file.read()

    image_tags = re.findall(r'!\[(.*?)]\((.*?)\)', content)
    logging.debug(f"Found {len(image_tags)} image tags")

    for alt_text, image_file in image_tags:
        if image_file.endswith('.png'):
            target_location = generate_target_location()

            source_path = os.path.join(os.path.dirname(blog_post_path), image_file)
            target_path = os.path.join('static', target_location)

            logging.debug(f"Moving image from {source_path} to {target_path}")

            os.makedirs(os.path.dirname(target_path), exist_ok=True)

            if not os.path.exists(source_path):
                logging.warning(f"Can't find file {source_path}")
                continue

            shutil.move(source_path, target_path)

            old_tag = f'![{alt_text}]({image_file})'
            new_tag = f'![{target_location}](/{target_location})'
            content = content.replace(old_tag, new_tag)
            logging.info(f"Updated image tag: {old_tag} -> {new_tag}")

    with open(blog_post_path, 'w') as file:
        file.write(content)

    logging.info("Blog post processing completed")


def main(args):
    current_dir = os.getcwd()
    blog_post_path = os.path.join(current_dir, args.blog_post)

    if not os.path.exists(blog_post_path):
        logging.error(f"The file '{args.blog_post}' does not exist.")
        return

    process_blog_post(blog_post_path)


if __name__ == "__main__":
    args = parse_args()
    setup_logging(args.verbose)
    main(args)
