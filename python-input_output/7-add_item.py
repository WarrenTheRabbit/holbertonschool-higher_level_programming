#!/usr/bin/python3
"""Module contains a basic add item function."""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def add_item(*args):
    """Add item to a list and save to a file."""
    items = [arg for arg in sys.argv[1:]]
    obj = load_from_json_file("add_item.json")
    obj = obj + items
    save_to_json_file(obj, "add_item.json")
