#!/usr/bin/python3
"""Module contains a basic class to json function."""


def class_to_json(obj):
    """Return the JSON representation of an object (string)"""
    return json.dumps(obj.__dict__)
