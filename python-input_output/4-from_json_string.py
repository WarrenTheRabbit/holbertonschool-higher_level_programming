#!/usr/bin/python3
"""Module contains a basic from json string function."""
import json


def from_json_string(my_str):
    """Return the JSON representation of an object (string)"""
    return json.loads(my_str)
