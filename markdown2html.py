#!/usr/bin/python3
"""
Markdown to HTML Converter

Usage: ./markdown2html.py <input_file> <output_file>
"""
import sys
import os
import markdown


def convert_markdown_to_html(input_file, output_file):
    """
    Convert Markdown to HTML and save it to the output file

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.
    """
    try:
        with open(input_file, 'r') as md_file:
            markdown_text = md_file.read()
            html = markdown.markdown(markdown_text)

        with open(output_file, 'w') as html_file:
            html_file.write(html)
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
