import tkinter as tk

from view.components.diagram import Diagram


class Toolbar(tk.Frame):
    def __init__(self, master):
        super().__init__()
        # will be elder of buttons diagram actions