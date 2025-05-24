# IntelliSnip
A lightweight command-line tool designed to help developers quickly retrieve commonly used code snippets in Python and Java.
It reads from structured JSON files and provides snippet lookup based on language and keyword.

## Features
- Supports both **Python** and **Java** code snippets
- Easy-to-use CLI interface
- Fast search with partial keyword matching
- --list feature to explore all available snippets per language
- Snippets organized in JSON for easy expansion


## 📂 Project Structure
```
intellisnip/
├── python/
│   ├── main.py         # CLI entry point
│   └── utils/
│       └── matcher.py  # Snippet search logic
├── snippets/
│   ├── python.json     # Python code snippets
│   └── java.json       # Java code snippets
├── README.md           # Project readme
```

## Usage - Search for a snippet
python python/main.py --lang python --query gcd
python python/main.py --lang java --query reverse

### List all snippets
python python/main.py --lang python --list
python python/main.py --lang java --list

## How It Works
- The command line interface reads JSON files from the `snippets/` folder.
- It searches snippet keys and descriptions based on user input.
- It returns formatted code blocks directly in the terminal.

## Adding Snippets
1. Open `snippets/python.json` or `snippets/java.json`
2. Add a new object with `description` and `code`
3. Save and run a search query to test

## Requirements
- Python 3.6+
- No external libraries required (pure standard library)

## How To Run/Use
In command prompt (cmd), go to the 'intellisnip' folder
if you need a snippet for gcd in python, type:
    python python/main.py --lang python --query gcd
if you want a list of all the snippets in python:
    python python/main.py --lang python --list
if you need a need a snippet for palindrome in Java:
    python python/main.py --lang java --query palindrome
