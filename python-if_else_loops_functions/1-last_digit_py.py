#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    message = "and is 0"
elif number > 5:
    message = "and is greater than 5"
else:
    message = "and is less than 6 and not 0"
print(f"Last digit of {str(number)[-1] } {message}