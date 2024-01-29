#!/usr/bin/python3
for i in range(97, 123):
    if not chr(i) in ['q', 'e']:
        print("{}".format(chr(i)), end="")
