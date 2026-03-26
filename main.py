import tkinter as tk

from utils.center_window import center_window

from controller.view_manger import ViewManager


class Nodes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.geometry("800x600")
        # self.center_window()
        center_window(self)

        self.deiconify()
        # self.update()

        self.bind("<Escape>", lambda e: self.quit())

        self.view_manager = ViewManager(self)

        # self.center_window()
        
        
        # self.deiconify()

if __name__ == "__main__":
    nodes = Nodes()
    nodes.mainloop()


        