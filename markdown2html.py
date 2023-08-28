#!/usr/bin/python3
"""
Markdown to HTML Converter

Usage: ./markdown2html.py <input_file> <output_file>
"""
import sys
import os
import markdown
import re


def convert_markdown_to_html(input_file, output_file):
    """
    Convert Markdown to HTML and save it to the output file

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.
    """
    try:
        # Open and read the input Markdown file
        with open(input_file, 'r') as md_file:
            markdown_text = md_file.read()

        # Define a regular expression pattern to match Markdown headings
        heading_pattern = re.compile(r'^(#+) (.+)$', re.MULTILINE)
        # Convert Markdown headings to HTML headings
        markdown_text = heading_pattern.sub(r'<h\1>\2</h\1>', markdown_text)

        # Convert Markdown to HTML
        html = markdown.markdown(markdown_text)

        # Write the HTML content to the output file
        with open(output_file, 'w') as html_file:
            html_file.write(html)
    except FileNotFoundError:
        # Handle the case where the input file is not found
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print(
            "Usage: ./markdown2html.py <input_file> <output_file>",
            file=sys.stderr)
        sys.exit(1)

    # Extract input and output file paths from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists; if not, display an error message and exit
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML and save it to the output file
    convert_markdown_to_html(input_file, output_file)

    # Exit with a successful status code
    sys.exit(0)
