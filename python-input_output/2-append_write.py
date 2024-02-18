#!/usr/bin/python3

"""Module contains a basic append write function."""


def append_write(filename="", text=""):
    """Wire file and print to stdout"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
