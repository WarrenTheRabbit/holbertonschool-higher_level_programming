#!/usr/bin/python3
"""Module contains a basic to json string function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)"""
    return json.dumps(my_obj)
