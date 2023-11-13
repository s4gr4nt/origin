#!/usr/bin/env python3

count = 0

with open("dracula.txt", "r") as read1:
    with open("vampytimes.txt", "w") as fang:
        for i in read1:
            if "vampire" in i.lower():
                print(i)
                count += 1
                fang.write(i)
print(count)
