#!/usr/bin/python3
"""
Markdown to HTML Converter

Usage: ./markdown2html.py <input_file> <output_file>
"""
import re
import os
import sys


def convert_markdown_to_html(md, html):
    """
    Converts a Markdown file to HTML.

    Args:
        md (str): Path to the input Markdown file.
        html (str): Path to the output HTML file.
    """
    # Check if the input Markdown file exists
    if not os.path.exists(md):
        print(f"Missing {md}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(md, encoding="utf-8") as f:
        html_lines = []
        inside_list = False  # Flag to track if we are inside a list

        for line in f:
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(
                    f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                # Check for unordered lists
                if re.match(r"^- ", line):
                    # If not inside a list, start a new list
                    if not inside_list:
                        html_lines.append("<ul>")
                        inside_list = True
                    # Extract the list item and add it to the HTML
                    list_item = line[2:].strip()
                    html_lines.append(f"<li>{list_item}</li>")
                else:
                    # If we were inside a list, close it
                    if inside_list:
                        html_lines.append("</ul>")
                        inside_list = False
                    html_lines.append(line.rstrip())

        # Close any open list at the end of the document
        if inside_list:
            html_lines.append("</ul>")

    # Write the HTML output to a file
    with open(html, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))


if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(sys.argv[1], sys.argv[2])

    # Exit with a successful status code
    sys.exit(0)
