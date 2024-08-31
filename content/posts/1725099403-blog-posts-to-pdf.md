+++ 
date = 2024-08-31T11:16:44+01:00
title = "From Website to PDF using Vivaldi Browser and SingleFile extension"
description = "A comprehensive guide to converting web pages into a single PDF document using Vivaldi Browser, SingleFile extension, and Python scripts. This tutorial covers downloading complete HTML files, cleaning up unwanted tags, converting HTML to PDF, and merging multiple PDFs into one."
slug = "" 
tags = ["web scraping", "PDF conversion", "SingleFile", "Python", "pandoc"]
categories = ["automation"]
externalLink = ""
series = []
+++

### Pre-Requisites:

* Vivaldi Browser (Although any other browser can be used)
* [SingleFile extension](https://github.com/gildas-lormeau/SingleFile)

If using Chrome then [single-file-cli](https://github.com/gildas-lormeau/single-file-cli) should also work,
but it didn't work with Vivaldi.

**Start with a collection of links in a file**

```
link1.html
link2.html
```

**Download complete HTML for each url** 

Note: Change the x,y coordinates if required

[Github](https://github.com/namuan/bin-utils/blob/master/download-urls.py)

```python
#!/usr/bin/env python3
"""
A script to download web pages using Vivaldi browser and SingleFile extension

Usage:
./download-urls.py -h

./download-urls.py -v file.txt # To log INFO messages
./download-urls.py -vv file.txt # To log DEBUG messages
"""
import logging
import subprocess
import time
from argparse import ArgumentParser, RawDescriptionHelpFormatter

import pyautogui


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
        "file",
        help="File containing list of URLs",
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


def open_vivaldi(url):
    subprocess.Popen(["open", "-a", "Vivaldi", url])


def process_url(url):
    # Set the coordinates where you want to click
    single_file_x, single_file_y = 1493, 92
    click_x, click_y = 1489, 287

    logging.info(f"Opening Vivaldi with URL: {url}")
    open_vivaldi(url)

    # Wait for the page to load
    time.sleep(5)

    logging.debug(f"Moving to coordinates: ({single_file_x}, {single_file_y})")
    pyautogui.moveTo(single_file_x, single_file_y)

    logging.debug("Clicking at current position")
    pyautogui.click()

    logging.debug(f"Moving to coordinates: ({click_x}, {click_y})")
    pyautogui.moveTo(click_x, click_y)

    logging.info("Waiting for 15 seconds")
    time.sleep(15)


def main(args):
    # Ensure a safe exit is possible
    pyautogui.FAILSAFE = True

    # Initial delay before starting the process
    logging.info("Starting initial delay of 5 seconds")
    time.sleep(5)

    try:
        with open(args.file) as f:
            urls = f.read().splitlines()

        logging.info(f"Found {len(urls)} URLs in the file")

        for i, url in enumerate(urls, 1):
            logging.info(f"Processing URL {i} of {len(urls)}: {url}")
            process_url(url)

        logging.info("Script completed successfully.")

    except KeyboardInterrupt:
        logging.warning("Script terminated by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    args = parse_args()
    setup_logging(args.verbose)
    main(args)
```

**Clean up any unwanted tags**

```python
import os
import re

def clean_html_files(directory):
    # Pattern for iframes
    iframe_pattern = re.compile(r'<iframe.*?</iframe>', re.DOTALL)

    # Pattern for dir=ltr
    dir_ltr_pattern = re.compile(r'\s*dir=ltr\s*')

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            # Remove iframes and dir=ltr
            modified_content = iframe_pattern.sub('', content)
            modified_content = dir_ltr_pattern.sub('', modified_content)

            if content != modified_content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(modified_content)
                print(f"Processed: {filename}")

# Use the current directory
current_directory = os.getcwd()
clean_html_files(current_directory)
```

**Convert individual HTML file to PDF**

```shell
#!/bin/bash

# Set the directory containing the HTML files
html_dir="$HOME/temp/lazy-trader"
pdf_dir="$html_dir/pdf"

# Create the pdf subdirectory if it doesn't exist
mkdir -p "$pdf_dir"

# Iterate over each HTML file in the directory
for html_file in "$html_dir"/*.html; do
  # Check if there are any matching files
  if [ ! -e "$html_file" ]; then
    echo "No HTML files found in $html_dir"
    exit 1
  fi

  # Extract the filename without the extension
  filename=$(basename "$html_file" .html)
  printf "Converting %s to %s.pdf\n" "$html_file" "$filename"

  # Convert the HTML file to PDF using pandoc
  pandoc "$html_file" -o "$pdf_dir/$filename.pdf"

  # Print a message indicating the conversion is complete
  echo "Converted $html_file to $pdf_dir/$filename.pdf"
done

echo "All PDF files have been saved in $pdf_dir"
```

**Merge into one PDF**

```shell
pip install PyPDF2
```

```python
import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_directory, output_filename):
    merger = PdfMerger()

    # Get all PDF files in the directory
    pdf_files = [f for f in os.listdir(input_directory) if f.endswith(".pdf")]
    
    # Sort the files to ensure a consistent order
    pdf_files.sort()

    # Append each PDF file to the merger
    for filename in pdf_files:
        filepath = os.path.join(input_directory, filename)
        merger.append(filepath)

    # Write the merged PDF to the output file
    with open(output_filename, "wb") as output_file:
        merger.write(output_file)

    print(f"Merged {len(pdf_files)} PDF files into {output_filename}")

# Set up the paths
current_directory = os.getcwd()
input_directory = os.path.join(current_directory, "pdf-output")
output_file = os.path.join(current_directory, "merged_output.pdf")

# Check if the pdf-output directory exists
if not os.path.exists(input_directory):
    print(f"Error: The directory '{input_directory}' does not exist.")
else:
    merge_pdfs(input_directory, output_file)
```

The final copy will be in `merged_output.pdf` file in the current directory
