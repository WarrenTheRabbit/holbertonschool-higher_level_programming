#!/usr/bin/python3
"""Module contains a basic save to json file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write JSON representation of an object to a file."""
    json.dump(my_obj, filename)
