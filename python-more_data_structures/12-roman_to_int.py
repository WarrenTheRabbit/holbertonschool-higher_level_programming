#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    conversion = {
        "X": 10,
        "V": 5,
        "L": 50,
        "I": 1,
        "C": 100,
        "D": 500,
    }

    values = [conversion[symbol] for symbol in roman_string]
    total = 0

    for i in range(len(values)):
        if i + 1 < len(values) and values[i] < values[i+1]:
            total -= values[i]
        else:
            total += values[i]
    return total
