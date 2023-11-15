#!/usr/bin/env python3

import random
import tkinter as tk
from tkinter import font

def display_options(seasons, weather):
    root = tk.Tk() #creates the root window (main window)
    root.geometry("1080x720")
    root.configure(bg="#17496c")
    root.title("Trip Ideas & Decision Maker") #you will see this at the top left of your window

    custom_font = font.Font(family="Ink Free", size=16, weight="bold")
    label1 = tk.Label(root, font=custom_font, fg="#779fba", text="What season are we in today? (spring, summer, fall, winter): ")
    label1.configure(bg="#17496c")
    label1.pack(pady=10)

    entry1 = tk.Entry(root, font=custom_font, width=30) # Entry for the custom day greeting.
    entry1.pack(pady=20)
    


    label2 = tk.Label(root, font=custom_font, bg="#17496c", fg="#779fba", text="What is the weather like? (rainy, sunny, snowy): ")
    label2.pack(pady=10)

    entry2 = tk.Entry(root, font=custom_font, width=30)
    entry2.pack(pady=20)

    result_text = tk.Text(root, font=custom_font, height=10, width=70)
    result_text.pack(pady=20)

    def make_decision():
        R1seasons = entry1.get().lower()
        R2weather = entry2.get().lower()

        options = get_options(R1seasons, R2weather)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, options)

    button = tk.Button(root, font=custom_font, text="Make Decision", command=make_decision)
    button.pack()

    root.mainloop()

def get_options(season, weather):
    # Options according to seasons
    spring = ["Washington State University cherry blossoms", "Skagit Valley Tulip Festival", "Scenic Hot Springs", "Snoqualmie Falls", "Colchuck Lake"]
    indspring = ["Stay at a Cabin", "Cafe and Library/Bookstore", "B&B", "Indoor Hot Springs"]

    summer = ["Dog Mountain", "Fishing", "Camping", "Hoh Rainforest", "Bellevue Botanical Garden", "Berry/Fruit Picking"]
    indsummer = ["Wine Tasting", "Stay at a Cabin", "Chihuly Garden and Glass"]

    fall = ["Pumpkin Patch", "Scenic Hot Springs", "Lake Chelan", "Apple Picking"]
    indfall = ["Cafe and Library/Bookstore", "Go to a bar and B&B nearby", "Replacing/Tending to plants"]

    winter = ["Reindeer Farm", "Wenatchee", "Mt. Rainier", "Trip to Canada", "Stevens Pass", "Pike Place Market"]
    indwinter = ["Make special warm drinks at home", "Movie/Show Marathon", "Bake 3 pastries", "PJ party", "Create/Craft something for the new year", "Shopping"]

    # Describe weather options
    weather_options = ["rainy", "sunny", "snowy"]

    options = ""

    # Conditions set according to seasons
    if season == "spring" and weather == weather_options[0]:
        options = "\n".join(indspring)
    elif season == "spring" and weather == weather_options[1]:
        options = "\n".join(spring)
    elif season == "summer" and weather == weather_options[0]:
        options = "\n".join(indsummer)
    elif season == "summer" and weather == weather_options[1]:
        options = "\n".join(summer)
    elif season == "fall" and weather == weather_options[0]:
        options = "\n".join(indfall)
    elif season == "fall" and weather == weather_options[1]:
        options = "\n".join(fall)
    elif season == "winter" and weather == weather_options[0]:
        options = "\n".join(indwinter)
    elif season == "winter" and weather == weather_options[1]:
        options = "\n".join(winter)
    elif season == "winter" and weather == weather_options[2]:
        options = "\n".join(indwinter)
    else:
        options = "Invalid input. Please enter valid season and weather."

    return options

if __name__ == "__main__":
    display_options([], [])
