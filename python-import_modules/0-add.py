#!/usr/bin/python3
import importlib

if __name__ == "__main__":
    func = importlib.import_module("0-add").add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, func(a, b)))
