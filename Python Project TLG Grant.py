#!/usr/bin/env python3

"""Python Project TLG | Stephanie Grant"""


import tkinter as tk
from tkinter import font
import json
import sys
import os
from datetime import date
import random
import pickle
#import requests


### Changing default path for reference of files
target_default = r"C:\Users\steph\Python Portfolio\Virtual Assistant Python Project"
os.chdir(target_default)


sys.setrecursionlimit(100000)  # Set a higher limit


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        today = date.today()

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Welcome to Your Virtual Assistant.")
        label.pack(pady=20)
        
        label2 = tk.Label(self, font=font3, bg="#eddcd2", text=f"TODAY'S DATE:  {today}")
        label2.pack(pady=5)

        label1 = tk.Label(self, font=font3, bg="#fff1e6", text="What would you like to do today?")
        #label1.configure(bg="#2c3968")
        label1.pack(pady=20)
        
        

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Bucket List", command=lambda: controller.show_frame(Bucketlist))
        button.pack(pady=10)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Travel", command=lambda: controller.show_frame(Travel))
        button.pack(pady=10)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Projects", command=lambda: controller.show_frame(Projects))
        button.pack(pady=10)
    
###################### FILE MANAGER ##########################
class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def write(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)
    
    def read(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file '{self.file_path}'.")
            return None

#################### BUCKETLIST!!! ###########################

class Bucketlist(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="BucketList Options")
        label.pack(pady=10)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Add or Remove", command=lambda: controller.show_frame(AddOrRemoveBucketlist))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="View Bucketlist", command=lambda: controller.show_frame(ViewBucketlist))
        button.pack(pady=5)

class AddOrRemoveBucketlist(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Add or remove contents to your bucketlist!")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list

        #with open("VA_data.pkl", "rb") as string_list:
         #   self.string_list = pickle.load(string_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, bg="#eddcd2", font=font3, text="Add", command=self.add_string)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, bg="#eddcd2", font=font3, text="Remove", command=self.rm_string)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, bg="#eddcd2", font=font3, text="Save", command=self.save_data)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Bucketlist))
        button.pack(pady=5)
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")
    
    def add_string(self):
        new_string = self.entry_var.get()
        if new_string:
            self.string_list.append(new_string)
            self.update_listbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_string(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            selected_item = self.string_list[selected[0]]
            self.string_list.remove(selected_item)

    def populate_listbox(self):
        for item in self.string_list:
            self.listbox.insert(tk.END, item)

    def save_data(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.string_list, file)
        print("Data saved successfully.")    


class ViewBucketlist(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="What have you completed so far?")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list     
        
        #with open("VA_data.pkl", "rb") as string_list:
        #   self.string_list = pickle.load(string_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Bucketlist))
        button.pack(pady=5)
        
        #button - tk.Button(self, text="Refresh")
        #button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Add or Remove", command=lambda: controller.show_frame(AddOrRemoveBucketlist))
        button.pack(pady=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")
            
####################### TRAVEL!!! #########################

class Travel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Travel Options")
        label.pack(pady=10)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Let's go somewhere!", command=lambda: controller.show_frame(Go))
        button.pack(pady=30)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Spring Activities", command=lambda: controller.show_frame(Spring))
        button.pack(pady=5)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Summer Activities", command=lambda: controller.show_frame(Summer))
        button.pack(pady=5)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Fall Activities", command=lambda: controller.show_frame(Fall))
        button.pack(pady=5)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Winter Activities", command=lambda: controller.show_frame(Winter))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        button.pack(pady=25)

class Go(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="I see you need help with deciding what to do today.")
        label.pack(pady=10)

        label1 = tk.Label(self, font=font2, bg="#fff1e6", text="Choose among the four seasons below and I can help you with today's agenda!")
        label1.pack()

        label2 = tk.Label(self, font=font2, bg="#fff1e6", text="Otherwise, you may go back to the main menu with the 'Back to Travel Menu'.")
        label2.pack()

        result_text = tk.Text(self, font=font2, height=10, width=70)
        result_text.pack(pady=20)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Spring Activities")
        button.pack(pady=5)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Summer Activities")
        button.pack(pady=5)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Fall Activities")
        button.pack(pady=5)

        button = tk.Button(self, font=font1, bg="#eddcd2", text="Winter Activities")
        button.pack(pady=5)

        button = tk.Button(self, font=font2, bg="#eddcd2", text="Back to Travel Menu", command=lambda: controller.show_frame(Travel))
        button.pack(pady=20)

    #def decidefactor():
        #api_key = "YOUR_API_KEY"
        #city = "YOUR_CITY"
        #base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        #response = requests.get(base_url)
        #data = response.json()

        # Extract relevant weather information
        #temperature = data['main']['temp']
        #weather_condition = data['weather'][0]['main']

        #if temperature -= '40' and weather_condition == ####:
            #springchoice = random.choice(FILE FROM SpringInOpt)




###SPRING###
class Spring(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")


        label = tk.Label(self, font=font1, bg="#fff1e6", text="Spring Activities")
        label.pack(pady=20)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back to Travel Menu", command=lambda: controller.show_frame(Travel))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Modify Outdoor Spring Activities", command=lambda: controller.show_frame(SpringOpt))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Modify Indoor Spring Activities", command=lambda: controller.show_frame(SpringInOpt))
        button.pack(pady=5)


class SpringOpt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Modify your Outdoor Spring Activities as you want!")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list

        #with open("VA_data1.pkl", "rb") as pstring_list:
        #    self.pstring_list = pickle.load(pstring_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Add", command=self.add_string)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Remove", command=self.rm_string)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, font=font3, bg="#eddcd2", text="Save", command=self.save_data)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Spring))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Indoor Spring Activities", command=lambda: controller.show_frame(SpringInOpt))
        button.pack(pady=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")
    
    def add_string(self):
        new_string = self.entry_var.get()
        if new_string:
            self.string_list.append(new_string)
            self.update_listbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_string(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            selected_item = self.string_list[selected[0]]
            self.string_list.remove(selected_item)

    def populate_listbox(self):
        for item in self.string_list:
            self.listbox.insert(tk.END, item)

    def save_data(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.string_list, file)
        print("Data saved successfully.")

class SpringInOpt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Modify your Indoor Spring Activities as you want!")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list

        #with open("VA_data1.pkl", "rb") as pstring_list:
        #    self.pstring_list = pickle.load(pstring_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Add", command=self.add_string)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Remove", command=self.rm_string)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, font=font3, bg="#eddcd2", text="Save", command=self.save_data)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Spring))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Outdoor Spring Activities", command=lambda: controller.show_frame(SpringOpt))
        button.pack(pady=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")

    def add_string(self):
        new_string = self.entry_var.get()
        if new_string:
            self.string_list.append(new_string)
            self.update_listbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_string(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            selected_item = self.string_list[selected[0]]
            self.string_list.remove(selected_item)

    def populate_listbox(self):
        for item in self.string_list:
            self.listbox.insert(tk.END, item)

    def save_data(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.string_list, file)
        print("Data saved successfully.")


###SUMMER###
class Summer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Summer Activities")
        label.pack(pady=10)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back to Travel Menu", command=lambda: controller.show_frame(Travel))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Modify Outdoor Summer Activities", command=lambda: controller.show_frame(SummerOpt))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Modify Indoor Summer Activities", command=lambda: controller.show_frame(SummerInOpt))
        button.pack(pady=5)

class SummerOpt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Modify your Outdoor Summer Activities as you want!")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list

        #with open("VA_data1.pkl", "rb") as pstring_list:
        #    self.pstring_list = pickle.load(pstring_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Add", command=self.add_string)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Remove", command=self.rm_string)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, font=font3, bg="#eddcd2", text="Save", command=self.save_data)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Summer))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Indoor Summer Activities", command=lambda: controller.show_frame(SummerInOpt))
        button.pack(pady=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")
    
    def add_string(self):
        new_string = self.entry_var.get()
        if new_string:
            self.string_list.append(new_string)
            self.update_listbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_string(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            selected_item = self.string_list[selected[0]]
            self.string_list.remove(selected_item)

    def populate_listbox(self):
        for item in self.string_list:
            self.listbox.insert(tk.END, item)

    def save_data(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.string_list, file)
        print("Data saved successfully.")

class SummerInOpt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Modify your Indoor Summer Activities as you want!")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list

        #with open("VA_data1.pkl", "rb") as pstring_list:
        #    self.pstring_list = pickle.load(pstring_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Add", command=self.add_string)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Remove", command=self.rm_string)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, font=font3, bg="#eddcd2", text="Save", command=self.save_data)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Summer))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Outdoor Summer Activities", command=lambda: controller.show_frame(SummerOpt))
        button.pack(pady=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")

    def add_string(self):
        new_string = self.entry_var.get()
        if new_string:
            self.string_list.append(new_string)
            self.update_listbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_string(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            selected_item = self.string_list[selected[0]]
            self.string_list.remove(selected_item)

    def populate_listbox(self):
        for item in self.string_list:
            self.listbox.insert(tk.END, item)

    def save_data(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.string_list, file)
        print("Data saved successfully.")


###FALL###
class Fall(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Fall Activities")
        label.pack(pady=10)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back to Travel Menu", command=lambda: controller.show_frame(Travel))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Modify Outdoor Fall Activities", command=lambda: controller.show_frame(FallOpt))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Modify Indoor Fall Activities", command=lambda: controller.show_frame(FallInOpt))
        button.pack(pady=5)

class FallOpt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Modify your Outdoor Fall Activities as you want!")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list

        #with open("VA_data1.pkl", "rb") as pstring_list:
        #    self.pstring_list = pickle.load(pstring_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Add", command=self.add_string)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Remove", command=self.rm_string)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, font=font3, bg="#eddcd2", text="Save", command=self.save_data)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Fall))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Indoor Fall Activities", command=lambda: controller.show_frame(FallInOpt))
        button.pack(pady=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")
    
    def add_string(self):
        new_string = self.entry_var.get()
        if new_string:
            self.string_list.append(new_string)
            self.update_listbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_string(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            selected_item = self.string_list[selected[0]]
            self.string_list.remove(selected_item)

    def populate_listbox(self):
        for item in self.string_list:
            self.listbox.insert(tk.END, item)

    def save_data(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.string_list, file)
        print("Data saved successfully.")

class FallInOpt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Modify your Indoor Fall Activities as you want!")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list

        #with open("VA_data1.pkl", "rb") as pstring_list:
        #    self.pstring_list = pickle.load(pstring_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Add", command=self.add_string)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Remove", command=self.rm_string)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, font=font3, bg="#eddcd2", text="Save", command=self.save_data)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Fall))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Outdoor Fall Activities", command=lambda: controller.show_frame(FallOpt))
        button.pack(pady=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")

    def add_string(self):
        new_string = self.entry_var.get()
        if new_string:
            self.string_list.append(new_string)
            self.update_listbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_string(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            selected_item = self.string_list[selected[0]]
            self.string_list.remove(selected_item)

    def populate_listbox(self):
        for item in self.string_list:
            self.listbox.insert(tk.END, item)

    def save_data(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.string_list, file)
        print("Data saved successfully.")

###WINTER###
class Winter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Winter Activities")
        label.pack(pady=10)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back to Travel Menu", command=lambda: controller.show_frame(Travel))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Modify Outdoor Winter Activities", command=lambda: controller.show_frame(WinterOpt))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Modify Indoor Winter Activities", command=lambda: controller.show_frame(WinterInOpt))
        button.pack(pady=5)

class WinterOpt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Modify your Outdoor Winter Activities as you want!")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list

        #with open("VA_data1.pkl", "rb") as pstring_list:
        #    self.pstring_list = pickle.load(pstring_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Add", command=self.add_string)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Remove", command=self.rm_string)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, font=font3, bg="#eddcd2", text="Save", command=self.save_data)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Winter))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Indoor Winter Activities", command=lambda: controller.show_frame(WinterInOpt))
        button.pack(pady=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")
    
    def add_string(self):
        new_string = self.entry_var.get()
        if new_string:
            self.string_list.append(new_string)
            self.update_listbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_string(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            selected_item = self.string_list[selected[0]]
            self.string_list.remove(selected_item)

    def populate_listbox(self):
        for item in self.string_list:
            self.listbox.insert(tk.END, item)

    def save_data(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.string_list, file)
        print("Data saved successfully.")


class WinterInOpt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Modify your Indoor Winter Activities as you want!")
        label.pack(pady=10)

        string_list = []
        self.string_list = string_list

        #with open("VA_data1.pkl", "rb") as pstring_list:
        #    self.pstring_list = pickle.load(pstring_list)

        self.listbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.listbox.pack(pady=20, padx=20)

        self.update_listbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Add", command=self.add_string)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Remove", command=self.rm_string)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, font=font3, bg="#eddcd2", text="Save", command=self.save_data)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Winter))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Outdoor Winter Activities", command=lambda: controller.show_frame(WinterOpt))
        button.pack(pady=5)


    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox
        for item in self.string_list:
            self.listbox.insert(tk.END, f"* {item}")

    def add_string(self):
        new_string = self.entry_var.get()
        if new_string:
            self.string_list.append(new_string)
            self.update_listbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_string(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            selected_item = self.string_list[selected[0]]
            self.string_list.remove(selected_item)

    def populate_listbox(self):
        for item in self.string_list:
            self.listbox.insert(tk.END, item)

    def save_data(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.string_list, file)
        print("Data saved successfully.")



################################################

class Projects(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Projects Options")
        label.pack(pady=10)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        button.pack()

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Add or Remove", command=lambda: controller.show_frame(AddOrRemoveProjects))
        button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="View Projects List", command=lambda: controller.show_frame(ViewProjects))
        button.pack(pady=5)

class AddOrRemoveProjects(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="Modify your Projects List as you want!")
        label.pack(pady=10)

        pstring_list = []
        self.pstring_list = pstring_list

        #with open("VA_data1.pkl", "rb") as pstring_list:
        #    self.pstring_list = pickle.load(pstring_list)

        self.plistbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.plistbox.pack(pady=20, padx=20)

        self.update_plistbox()

        self.entry_var = tk.StringVar()
        entry = tk.Entry(self, font=font2, textvariable=self.entry_var, width=150)
        entry.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Add", command=self.add_pstring)
        add_button.pack(pady=5, padx=10)

        add_button = tk.Button(self, font=font3, bg="#eddcd2", text="Remove", command=self.rm_pstring)
        add_button.pack(pady=5, padx=10)

        save_button = tk.Button(self, font=font3, bg="#eddcd2", text="Save", command=self.save_pdata)
        save_button.pack(pady=5) 

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Projects))
        button.pack(pady=5)
    
    def update_plistbox(self):
        self.plistbox.delete(0, tk.END)  # Clear the listbox
        for item in self.pstring_list:
            self.plistbox.insert(tk.END, f"* {item}")
    
    def add_pstring(self):
        pnew_string = self.entry_var.get()
        if pnew_string:
            self.pstring_list.append(pnew_string)
            self.update_plistbox()
            self.entry_var.set("")  # Clear the entry widget after adding
    
    def rm_pstring(self):
        selected = self.plistbox.curselection()
        if selected:
            self.plistbox.delete(selected)
            selected_item = self.pstring_list[selected[0]]
            self.pstring_list.remove(selected_item)

    def populate_plistbox(self):
        for item in self.pstring_list:
            self.plistbox.insert(tk.END, item)

    def save_pdata(self):
        with open("VA_data.pkl", "wb") as file:
            pickle.dump(self.pstring_list, file)
        print("Data saved successfully.")

class ViewProjects(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#fff1e6")
        self.controller = controller

        font1 = font.Font(family="Ink Free", size=20, weight="bold")
        font2 = font.Font(family="Ink Free", size=10, weight="bold")
        font3 = font.Font(family="Ink Free", size=15, weight="bold")

        label = tk.Label(self, font=font1, bg="#fff1e6", text="How are you doing with your projects?")
        label.pack(pady=10)

        pstring_list = []
        self.pstring_list = pstring_list     
        
        #with open("VA_data.pkl", "rb") as string_list:
        #   self.string_list = pickle.load(string_list)

        self.plistbox = tk.Listbox(self, font=font2, width=150, height=30)
        self.plistbox.pack(pady=20, padx=20)

        self.update_plistbox()

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Back", command=lambda: controller.show_frame(Projects))
        button.pack(pady=5)
        
        #button - tk.Button(self, text="Refresh")
        #button.pack(pady=5)

        button = tk.Button(self, font=font3, bg="#eddcd2", text="Add or Remove", command=lambda: controller.show_frame(AddOrRemoveProjects))
        button.pack(pady=5)

    def update_plistbox(self):
        self.plistbox.delete(0, tk.END)  # Clear the listbox
        for item in self.pstring_list:
            self.plistbox.insert(tk.END, f"* {item}")


###########################################

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self, bg="#cb997e")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Bucketlist, AddOrRemoveBucketlist, ViewBucketlist):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Bucketlist)

        for F in (Projects, AddOrRemoveProjects, ViewProjects):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Projects)

        for F in (MainMenu, Bucketlist, AddOrRemoveBucketlist, Travel, Projects, ViewBucketlist, AddOrRemoveProjects, ViewProjects, 
                  Spring, SpringOpt, SpringInOpt, Summer, SummerOpt, SummerInOpt, Fall, FallOpt, FallInOpt, Winter, WinterOpt, WinterInOpt, Go):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1260x900")
    app.title("Virtual Assistant")

    app.mainloop()