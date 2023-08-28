#!/usr/bin/python3
"""
Markdown to HTML Converter
"""
import re
import os
import sys


def convert_markdown_to_html(md_path, html_path):
    """
    Converts a Markdown file to HTML.

    Args:
        md_path (str): Path to the input Markdown file.
        html_path (str): Path to the output HTML file.
    """
    if not os.path.exists(md_path):
        print(f"Missing {md_path}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(md_path, 'r', encoding="utf-8") as md_file:
        md_lines = md_file.readlines()

    html_lines = [re.sub(r"^(#+) (.*)$",
                         r"<h\1>\2</h\1>", line) for line in md_lines]

    # Write the HTML output to a file
    with open(html_path, 'w', encoding="utf-8") as html_file:
        html_file.writelines(html_lines)


if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)
    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(sys.argv[1], sys.argv[2])

    # Exit with a successful status code
    sys.exit(0)
