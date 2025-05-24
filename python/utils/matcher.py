# python/utils/matcher.py

import json
import os

def get_snippet(lang, query):
    try:
        #intellisnip/python/utils/
        script_dir = os.path.dirname(os.path.abspath(__file__))
        #Up two levels to intellisnip/
        project_root = os.path.dirname(os.path.dirname(script_dir))
        path = os.path.join(project_root, "snippets", f"{lang}.json")

        #if the snippet file does not exist, return an error
        if not os.path.exists(path):
            return [], f"Snippets file for language '{lang}' not found."

        #load the JSON snippet data
        with open(path, "r") as file:
            data = json.load(file)

            #validate that the file contains a dictionary
            if not isinstance(data, dict):
                return [], f"Snippets file for language '{lang}' is malformed."

            matches = []

            #iterate through all snippets in the file
            for key, value in data.items():
                #skip any malformed entries
                if not isinstance(value, dict) or "code" not in value or "description" not in value:
                    continue

                #partial Match Logic
                #check if the user's query partially matches the snippet key
                #OR appears anywhere in the snippet description
                if query.lower() in key.lower() or query.lower() in value["description"].lower():
                    matches.append((key, value["code"], value["description"]))

            #if any matches were found, return them
            if matches:
                return matches, None   # list of matches, no error occurred

            #if no matches, return a helpful message
            return [], f"No snippet found for query '{query}' in language '{lang}'."

    #specific handling for broken JSON files
    except json.JSONDecodeError:
        return [], f"Snippets file for language '{lang}' contains invalid JSON."

    #generic fallback for other issues (e.g., file permission)
    except Exception as e:
        return [], f"Error: {str(e)}"
