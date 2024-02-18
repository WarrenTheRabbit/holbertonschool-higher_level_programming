#!/usr/bin/python3
"""Module contains a basic add item function."""
from pathlib import Path
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item():
    """Add item to a list and save to a file."""
    filename = "add_item.json"
    path = Path(filename)

    if not path.is_file():
        save_to_json_file([], filename)

    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)


if __name__ == "__main__":
    add_item()
