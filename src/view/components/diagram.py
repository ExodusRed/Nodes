import tkinter as tk



class Diagram(tk.Canvas):
    def __init__(self, master):
        pass

    def draw_node(self, x: int, y: int, r: int = 15):
        self.create_oval(x - 15, y - 15, x + 15, y + 15)


    # acts as canvas
    # we need drawing functions for nodes and edges