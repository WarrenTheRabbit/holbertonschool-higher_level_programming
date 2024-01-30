#!/usr/bin/python3
def uppercase(str):
    for character in str:
        # determine if character lowercase
        if ord(character) >= 97 and ord(character) <= 122:
            print(chr(ord(character) - 32), end='')
        else:
            print(character, end='')
    print()
