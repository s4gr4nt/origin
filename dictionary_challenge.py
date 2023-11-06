#!/usr/bin/env python3


marvelchars= {
"Starlord":
  {"real name": "Peter Quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "Raven Darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "Bruce Banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


while True:
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ")
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ")

    char_name = char_name.capitalize()
    char_stat = char_stat.lower()

    if char_name in marvelchars and char_stat in marvelchars[char_name]:
        response = marvelchars[char_name][char_stat]
        print(f"{char_name}'s {char_stat} is {response}.")
    
    else:
        print("Character/statistic not found.")

    try_again = input("Do you want to try again? (yes/no): ")
    try_again = try_again.lower()

    if try_again != "yes":
        print("Okay. Good bye.")
        break





