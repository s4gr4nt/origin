#!/usr/bin/env python3

import random


def main():
    #Options according to seasons
    spring = ["Washington State University cherry blossoms", "Skagit Valley Tulip Festival", "Scenic Hot Springs", "Snoqualmie Falls", "Colchuck Lake",]
    indspring = ["Stay at a Cabin", "Cafe and Library/Bookstore", "B&B", "Indoor Hot Springs"]
    
    summer = [ "Dog Mountain", "Fishing", "Camping", "Hoh Rainforest", "Bellevue Botanical Garden", "Berry/Fruit Picking" ]
    indsummer = ["Wine Tasting","Stay at a Cabin", "Chihuly Garden and Glass"]
    
    fall = ["Pumpkin Patch", "Scenic Hot Springs", "Lake Chelan", "Apple Picking"]
    indfall = ["Cafe and Library/Bookstore", "Go to a bar and B&B nearby", "Replacing/Tending to plants"]

    winter = ["Reindeer Farm", "Wenatchee", "Mt. Rainier", "Trip to Canada", "Stevens Pass", "Pike Place Market"]
    indwinter = ["Make special warm drinks at home", "Movie/Show Marathon", "Bake 3 pastries", "PJ party", "Create/Craft something for the new year", "Shopping"]

    #Describe weather options
    weather = ["rainy", "sunny", "snowy"]

    print("Hello. I see you need help with your indecisiveness today.")
    R1seasons = input("What season are we in today? (spring, summer, fall, winter): ")
    R2weather = input("What is the weather like? (rainy, sunny, snowy): ")
    # R3temp = input("What is the current temperature in Fahrenheit? ")

    R1seasons = R1seasons.lower()
    R2weather = R2weather.lower()

# Conditions set according to seasons
    if R1seasons == "spring" and R2weather == weather[0]:
        print("------------------------------")
        print("You can do the following: ")
        for item in indspring:
            print(item)
    elif R1seasons == "spring" and R2weather == weather[1]:
        print("------------------------------")
        print("You can do the following: ")
        for item1 in spring:
            print(item1)
    elif R1seasons == "summer" and R2weather == weather[0]:
        print("------------------------------")
        print("You can do the following: ")
        for item2 in indsummer:
            print(item2)
    elif R1seasons == "summer" and R2weather == weather[1]:
        print("------------------------------")
        print("You can do the following: ")
        for item3 in summer:
            print(item3)
    elif R1seasons == "fall" and R2weather == weather[0]:
        print("------------------------------")
        print("You can do the following: ")
        for item4 in indfall:
            print(item4)
    elif R1seasons == "fall" and R2weather == weather[1]:
        print("------------------------------")
        print("You can do the following: ")
        for item5 in fall:
            print(item5)
    elif R1seasons == "winter" and R2weather == weather[0]:
        print("------------------------------")
        print("You can do the following: ")
        for item6 in indwinter:
            print(item6)
    elif R1seasons == "winter" and R2weather == weather[1]:
        print("------------------------------")
        print("You can do the following: ")
        for item7 in winter:
            print(item7)
    elif R1seasons == "winter" and R2weather == weather[2]:
        print("------------------------------")
        print("You can do the following: ")
        for item6 in indwinter:
            print(item6)
    else:
        print("-------------")
        print("-------------")
        print("ERROR !!!!!!!!!!!!!!!!!!")
        print("If you think you're so smart to test me with an invalid answer, I believe you can go and figure this out yourself. Goodbye.")
        print("END PROGRAM")

if __name__ == "__main__":
    main()
