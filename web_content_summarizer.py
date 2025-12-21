#!/usr/bin/env -S uv run --quiet --script
# /// script
# dependencies = [
#   "litellm",
#   "trafilatura",
#   "beautifulsoup4",
# ]
# ///
"""
Web Content Summarizer

This script takes a file containing a list of URLs, extracts the content using JINA API,
summarizes it using Ollama via the litellm package, and generates a markdown file with the results.

Usage:
./web_content_summarizer.py -h
./web_content_summarizer.py -i input_links.txt -o output_summary.md -m ollama_chat/llama3.2
"""

import logging
import re
from argparse import ArgumentParser, RawDescriptionHelpFormatter

import requests
import trafilatura
from litellm import completion


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
        "-v", "--verbose", action="count", default=0, dest="verbose", help="Increase verbosity of logging output"
    )
    parser.add_argument("-i", "--input", required=True, help="Input file with list of links")
    parser.add_argument("-o", "--output", required=True, help="Output markdown file to write")
    parser.add_argument("-m", "--model", default="ollama_chat/llama3.2", help="Ollama model to use")
    return parser.parse_args()


def get_clean_page_content(url):
    try:
        downloaded = trafilatura.fetch_url(url)
        return trafilatura.extract(downloaded)
    except requests.RequestException as e:
        logging.error(f"Error fetching content from {url}: {e}")
        return None


def summarize_content(content, model_name):
    """
    Summarize the content using Ollama via litellm package.
    """
    prompt = f"""
Summarise the content using only bullet points in markdown syntax.
No headings, just bullet points.
I want it as raw markdown so that I can use it in README.md file
Make sure it is in raw markdown block to make it easy to copy

Content:\n\n
{content}
    """
    try:
        response = completion(
            model="openai/proxy",
            api_key="any_key_will_do",
            api_base="http://0.0.0.0:8080/v1",
            messages=[
                {"content": prompt, "role": "user"}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error summarizing content with {model_name}: {e}")
        return None


def extract_url(text):
    # Define the regex pattern to match text between ** and **
    pattern = r"\*\*(.*?)\*\*"

    # Search for the pattern in the input text
    match = re.search(pattern, text)

    # If a match is found, return the content between **; otherwise, return None
    return match.group(1) if match else None


def process_links(input_file, output_file, model):
    """
    Process links from input file, summarize content, and write to output file.
    """
    try:
        with open(input_file) as infile, open(output_file, "w") as outfile:
            outfile.write("# Web Content Summaries\n\n")
            for line in infile:
                if not "http" in line:
                    continue

                url = extract_url(line.strip())
                if not url:
                    continue

                logging.info(f"Processing: {url}")
                content = get_clean_page_content(url)
                if content:
                    summary = summarize_content(content, model)
                    if summary:
                        outfile.write(f"## {url}\n\n{summary}\n\n")
                    else:
                        outfile.write(f"## {url}\n\nFailed to summarize content.\n\n")
                else:
                    outfile.write(f"## {url}\n\nFailed to fetch content.\n\n")
    except OSError as e:
        logging.error(f"Error processing files: {e}")


def main(args):
    logging.info("Starting web content summarization")
    process_links(args.input, args.output, args.model)
    logging.info("Finished web content summarization")


if __name__ == "__main__":
    args = parse_args()
    setup_logging(args.verbose)
    main(args)
