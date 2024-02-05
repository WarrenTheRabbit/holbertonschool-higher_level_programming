#!/usr/bin/python3
def magic_string():
    nonlocal n
    for i in range(n):
        print(", ".join(["BestSchool"] * (i + 1)))
