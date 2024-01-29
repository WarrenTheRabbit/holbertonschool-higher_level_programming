#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = -1 if number < 0 else 1
if number == 0:
    message = "and is 0"
elif number > 5:
    message = "and is greater than 5"
else:
    message = "and is less than 6 and not 0"
print(f"Last digit of {number} is {sign * (abs(number) % 10)} {message}")
