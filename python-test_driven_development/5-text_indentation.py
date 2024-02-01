#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: .?:

    Args:
        text (str): text to be printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_line_needed = False
    for char in text:
        if new_line_needed and char == ' ':
            continue
        print(char, end='')
        new_line_needed = False
        if char in '.?:':
            print('\n\n', end='')
            new_line_needed = True
