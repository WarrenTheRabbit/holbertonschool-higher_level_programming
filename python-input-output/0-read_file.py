#!/usr/bin/python3

"""Module contains a basic read file function."""


def read_file(filename=""):
    """Read file and print to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
