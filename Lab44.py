#!/usr/bin/env python3
"""99 Bottles Song Project - Lab 44"""


import time

while True:  
    num = int(input("How many bottles of beer should we pass around? "))
    if num > 100:
        print("Choose a number equal to or less than 100!")

    elif num <= 0:
        print("Choose a number higher than 1!")

    else:
        for i in range(num, 0, -1):
            print(f"{i} bottles of beer on the wall!")
            time.sleep(1)
            print(f"{i} bottles of beer on the wall! {i} bottles of beer! You take one down, pass it around!")
            time.sleep(1)

