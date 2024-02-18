#!/usr/bin/python3
"""Module contains a basic load from json file function."""
import json


def load_from_json_file(filename):
    """Return the JSON representation of an object (string)"""
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
