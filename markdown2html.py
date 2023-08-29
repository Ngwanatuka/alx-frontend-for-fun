#!/usr/bin/python3
"""
Markdown to HTML Converter

Usage: ./markdown2html.py <input_file> <output_file>
"""
import hashlib
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
        inside_ordered_list = False
        inside_paragraph = False
        paragraph_lines = []  # Store lines within a paragraph

        for line in f:
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(
                    f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                # Check for ordered lists
                if re.match(r"^\* ", line):
                    # If not inside an ordered list, start a new list
                    if not inside_ordered_list:
                        html_lines.append("<ol>")
                        inside_ordered_list = True
                        # If we were inside a paragraph, close it
                        if inside_paragraph:
                            formatted_paragraph = format_paragraph(
                                paragraph_lines)
                            html_lines.append(formatted_paragraph)
                            paragraph_lines = []
                            html_lines.append("</p>")
                            inside_paragraph = False
                    # Extract the list item and add it to the HTML
                    list_item = line[2:].strip()

                    # Handle bold syntax within list items
                    list_item = re.sub(
                        r"\*\*(.*?)\*\*", r"<b>\1</b>", list_item)
                    html_lines.append(f"<li>{list_item}</li>")
                # Check for unordered lists
                elif re.match(r"^- ", line):
                    # If not inside a list, start a new list
                    if not inside_list:
                        html_lines.append("<ul>")
                        inside_list = True
                    # Extract the list item and add it to the HTML
                    list_item = line[2:].strip()

                    # Handle bold syntax within list items
                    list_item = re.sub(
                        r"\*\*(.*?)\*\*", r"<b>\1</b>", list_item)
                    html_lines.append(f"<li>{list_item}</li>")
                else:
                    # If it's a blank line, close the paragraph
                    if line.strip() == "":
                        # If we were inside an ordered list, close it
                        if inside_ordered_list:
                            html_lines.append("</ol>")
                            inside_ordered_list = False
                        # If we were inside a list, close it
                        if inside_list:
                            html_lines.append("</ul>")
                            inside_list = False
                        if inside_paragraph:
                            # Add lines within the paragraph with <br /> tags
                            for para_line in paragraph_lines:
                                html_lines.append(para_line)
                            # Reset paragraph lines
                            paragraph_lines = []
                            html_lines.append("</p>")
                            inside_paragraph = False

                    else:
                        # If we are not inside a paragraph, start one
                        if not inside_paragraph:
                            html_lines.append("<p>")
                            inside_paragraph = True
                        # Remove leading spaces
                        line = line.strip()

                        # Handle bold syntax
                        line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
                        # Handle italic syntax
                        line = re.sub(r"__(.*?)__", r"<em>\1</em>", line)

                        # Check for [[...]] syntax
                        match_md5 = re.search(r"\[\[(.*?)\]\]", line)
                        if match_md5:
                            md5_hash = hashlib.md5(match_md5.group(1).encode()).hexdigest()
                            line = line.replace(match_md5.group(0), md5_hash)

                        # Check for ((...)) syntax
                        match_remove_c = re.search(r"\(\((.*?)\)\)", line, flags=re.IGNORECASE)
                        if match_remove_c:
                            content_without_c = re.sub(r"c", "", match_remove_c.group(1), flags=re.IGNORECASE)
                            line = line.replace(match_remove_c.group(0), content_without_c)

                        if line:
                            """Add line to the paragraph lines with <br />
                              if it's not the first line
                            """
                            if paragraph_lines:
                                paragraph_lines.append("<br />")
                            paragraph_lines.append(line)

        # Close any open ordered list at the end of the document
        if inside_ordered_list:
            html_lines.append("</ol>")
        if inside_list:
            html_lines.append("</ul>")
        if inside_paragraph:
            # Add lines within the paragraph with <br /> tags
            for para_line in paragraph_lines:
                html_lines.append(para_line)
            html_lines.append("</p>")

    # Write the HTML output to a file
    with open(html, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines))


def format_paragraph(lines):
    """
    Format lines within a paragraph with bold and italic tags.

    Args:
        lines (list): List of lines within a paragraph.

    Returns:
        str: Formatted HTML paragraph.
    """
    formatted_lines = []
    for line in lines:
        # Handle bold syntax
        line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
        # Handle italic syntax
        line = re.sub(r"__(.*?)__", r"<em>\1</em>", line)
        formatted_lines.append(line)
    return "<br />".join(formatted_lines)


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
