import tkinter as tk

from controller.main_controller import MainController

class Nodes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Nodes")

        self.main_controller = MainController()

    
if __name__ == "__main__":
    nodes = Nodes()
    nodes.mainloop()
        
        