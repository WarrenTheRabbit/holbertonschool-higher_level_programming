#!/usr/bin/python3
def uppercase(str):
    result = ''
    for character in str:
        # determine if character lowercase
        if ord(character) >= 97 and ord(character) <= 122:
            result += chr(ord(character) - 32)
        else:
            result += character
    print("{}".format(result))
