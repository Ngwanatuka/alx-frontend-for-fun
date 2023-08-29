# Markdown to HTML Converter

This is a Python script that converts Markdown files into HTML format. It supports basic Markdown syntax and additional custom syntax for special formatting.

## Usage

To use the converter, follow these steps:

1. Make sure you have Python 3 installed on your system.

2. Download the `markdown2html.py` script and place it in the same directory as your Markdown file.

3. Open your terminal or command prompt.

4. Run the converter by executing the following command:
   
   ```bash
   ./markdown2html.py input.md output.html

* Replace input.md with the name of your Markdown file.
* Replace output.html with the desired name for the generated HTML file.

1. The converter will read your Markdown file, apply basic Markdown formatting, and save the result in an HTML file.

###Custom Syntax

This converter also supports custom syntax for special formatting:

To convert text to MD5 (lowercase), use double square brackets, like this: [[Hello]]. It will display the MD5 hash of the text.

To remove specific characters (case insensitive) from text, use double parentheses, like this: ((Hello Chicago)). It will remove all occurrences of 'c' from the text.

###Example
Here's an example of how the converter works:

###Input Markdown (input.md)

``` 
# My title
- He**l**lo
- Bye

Hello

I'm **a** text
with __2 lines__

((I will live in Caracas))

But it's [[private]]

So cool!
```

###Output HTML (output.html)

```
<h1>My title</h1>
<ul>
<li>He<b>l</b>lo</li>
<li>Bye</li>
</ul>
<p>
Hello
</p>
<p>
I'm <b>a</b> text
<br/>
with <em>2 lines</em>
</p>
<p>
I will live in araas
</p>
<p>
But it's 2c17c6393771ee3048ae34d6b380c5ec
</p>
<p>
So cool!
</p>

```

I did this for learning porpuses, from ALX AFRICA, and I'm very happy with the results, I hope you like it too.