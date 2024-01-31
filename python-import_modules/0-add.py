#!/usr/bin/python3
import importlib

def add(a, b):
    return a + b

# This would be in your main file, e.g., '0-add.py'
if __name__ == "__main__":
    func = importlib.import_module("0-add").add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
