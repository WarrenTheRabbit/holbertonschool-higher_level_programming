#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: .?:

    Args:
        text (str): text to be printed
    """
    did_newline = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    if not text:
        return
    for i in range(len(text)):
        if did_newline and text[i].isspace():
            did_newline = False
            continue
        if did_newline:
            did_newline = False
        if text[i] in ".?:":
            did_newline = True
            print(text[i])
            print()
        else:
            print(text[i], end="")
