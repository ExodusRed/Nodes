import tkinter as tk

class ViewController:
    def __init__(self, root):
        self.root = root

    def create_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        