#!/usr/bin/env python3

import random

heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
print(heroes)
print("My favorite character is", heroes[3] + "!")
# Example: My favorite character is Black Panther!


# PART 2
# Ask the user to pick a number between 1 and 100.
#input("Choose a number between 1 and 100: ")
num = int(input("Choose a number between 1 and 100: "))
# Convert the input into an integer.
print("You chose the number", num)

nums= [1, -5, 56, 987, 0]

# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!
largest_num = max(nums)
print("The largest number in set nums is:", largest_num)
