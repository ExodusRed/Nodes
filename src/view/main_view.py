import tkinter as tk

from view.components.toolbar import Toolbar
from view.components.diagram import Diagram

class MainView(tk.Frame):
    def __init__(self, view_controller):
        print("Initializing Main View.")
        super().__init__()

        self.name = "Main"

        self.toolbar = Toolbar(self)
        self.diagram = Diagram(self)

        

        