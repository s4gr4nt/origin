#!/usr/bin/env python3
"""Playing with Colors | Crayons Module | Lab 53"""
import crayons

def main():
    while True:
        print("What colors would you like to see? (red, yellow, blue, none)")
        choice = input("Color Choice: ")
        choice = choice.lower()

        if choice == "none":
            print("Okay. Goodbye.")
            break
        elif choice == "red":
            print(crayons.red('RED STRING', bold=True))
        elif choice == "yellow":
            print(crayons.yellow('YELLOW STRING', bold=True))
        elif choice == "blue":
            print(crayons.blue('BLUE STRING', bold=True))
        else:
            print("Please choose among the four given options only.")

if __name__ == "__main__":
    main()

