#!/usr/bin/python3

"""Module contains a basic write file function."""


def write_file(filename="", text=""):
    """Wire file and print to stdout"""
    with open(filename, "w", encoding='utf-8') as f:
        print(f.write(text))
