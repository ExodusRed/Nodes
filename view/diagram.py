import tkinter as tk

class Diagram(tk.Canvas):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)