#!/usr/bin/env python3

import tkinter as tk

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Outside Bucketlist")
        label.pack(pady=10)

        button = tk.Button(self, text="Bucket List", command=lambda: controller.show_frame(Bucketlist))
        button.pack()

class Bucketlist(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Inside Bucketlist")
        label.pack(pady=10)

        button_back = tk.Button(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        button_back.pack()

        button_add_remove = tk.Button(self, text="Add or Remove", command=lambda: controller.show_frame(AddOrRemove))
        button_add_remove.pack()

class AddOrRemove(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Add or remove contents to your bucketlist!")
        label.pack(pady=10)

        button_customize = tk.Button(self, text="Customize Your Bucketlist!", command=lambda: controller.show_frame(CustomBucketlist))
        button_customize.pack()

class CustomBucketlist(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Customize Your Bucketlist!")
        label.pack(pady=10)

        button_back = tk.Button(self, text="Back to Bucketlist", command=lambda: controller.show_frame(Bucketlist))
        button_back.pack()

class SampleController:
    def __init__(self, root):
        self.root = root

    def show_frame(self, frame_class):
        frame = frame_class(self.root, self)
        frame.tkraise()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")

    controller = SampleController(root)
    main_menu = MainMenu(root, controller)

    root.mainloop()
