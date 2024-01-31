#!/usr/bin/python3

import importlib

func = importlib.import_module('0-add').add
a = 1
b = 2
print("{} + {} = {}".format(a, b, func(1, 2)))
