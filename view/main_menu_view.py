import tkinter as tk

class MainMenuView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.create_ui()

        print("MainMenuView Inititalized.")

    def create_ui(self):
        tstLabel = tk.Label(self, text="Test")
        tstLabel.pack()