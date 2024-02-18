#!/usr/bin/python3
"""Module contains a basic save to json file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write JSON representation of an object to a file."""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
