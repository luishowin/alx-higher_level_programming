#!/usr/bin/python3
"""Define a func."""


import sys
import os
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_items_and_save(arguments):
    """
    Add command line arguments to a list, load existing items from a file,
    extend the list, and save it back to the file in JSON format.

    :param arguments: The command line arguments to add to the list.
    """
    try:
        # Load existing items from the file if it exists
        try:
            existing_items = load_from_json_file('add_item.json')
        except FileNotFoundError:
            existing_items = []

        # Add new items from command line arguments
        existing_items.extend(arguments)

        # Save the updated list to the file
        save_to_json_file(existing_items, 'add_item.json')

        print("Items successfully added and saved.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Skip the script name (sys.argv[0]) and pass the rest of the arguments
    add_items_and_save(sys.argv[1:])
