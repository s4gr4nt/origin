#!/usr/bin/env python3

import requests
import wget

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    choice = pokeapi["sprites"]["front_default"]

    # BONUS
    wget.download(choice, "/home/student/static/")

    print("Moves: ")
    for x in pokeapi["moves"]:
        x=x["move"]["name"]
        print(x)
    
    indices = pokeapi["game_indices"]
#    num = len(pokeapi["game_indices"])
    gamecount = 0
    for x in indices:
        gamecount +=1
    num = gamecount

    print(choice)
    print(f"The pokemon you see above appeared in {num} games.")
    print("Pokemon successfully downloaded.")

main()

