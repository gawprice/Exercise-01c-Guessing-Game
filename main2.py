#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
import random
number = random.randrange(1,10)
guess = input("Guess a number from 1 to 10: ")
guess = int(guess)
if guess == number:
    print("Great job! You got it!")
else:
    print("Sorry, better luck next time.")
    print("The number was " + str(number))