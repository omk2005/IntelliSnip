# python/main.py

import argparse
from utils.matcher import get_snippet

def main():
    parser = argparse.ArgumentParser(description="IntelliSnip: Code Snippet Generator")
    parser.add_argument('--lang', required=True, help='Programming language (e.g., java, python, cpp)')
    parser.add_argument('--query', help='Keyword or description (e.g., binary search, gcd)')
    parser.add_argument('--list', action='store_true', help='List all available snippets for the language')
    args = parser.parse_args()

    if args.list:
        list_snippets(args.lang.lower())
        return

    if not args.query:
        print("❌ Please provide a --query to search for snippets (or use --list to see available snippets).")
        return

    matches, error = get_snippet(args.lang.lower(), args.query.lower())

    if matches:
        print(f"\n🔹 Found {len(matches)} snippet(s) for '{args.query}' in {args.lang}:\n")
        for i, (key, code, description) in enumerate(matches, 1):
            print(f"Match {i} - {key}:")
            print(f"Description: {description}\n")
            print(f"Code:\n{code}\n")
    else:
        print(f"❌ {error}")

def list_snippets(lang):
    from os.path import join, dirname
    import json, os

    # Navigate up one level from python/ to the project root
    script_dir = dirname(os.path.abspath(__file__))  # intellisnip/python/
    project_root = dirname(script_dir)  # Up one level to intellisnip/
    path = join(project_root, "snippets", f"{lang}.json")

    if not os.path.exists(path):
        print(f"❌ Snippets file for '{lang}' not found.")
        return

    with open(path, "r") as file:
        data = json.load(file)
        if not isinstance(data, dict):
            print(f"❌ Snippet file for '{lang}' is malformed.")
            return

        print(f"\n📚 Snippets available for {lang}:\n")
        for key, val in sorted(data.items()):
            desc = val.get("description", "No description.")
            print(f"🔸 {key}: {desc}")

if __name__ == '__main__':
    main()