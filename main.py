import tkinter as tk

from controller.view_controller import ViewController


class Nodes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.geometry("800x600")
        self.center_window()

        self.bind("<Escape>", lambda e: self.quit())

        self.view_controller = ViewController(self)
        
        self.deiconify()

    def center_window(self):
        self.update_idletasks()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        ww, wh = self.winfo_width(), self.winfo_height()

        nw, nh = (sw // 2) - (ww // 2), (sh // 2) - (wh // 2)

        self.geometry(f"+{nw}+{nh - 30}") # -30 accomandation for taskbar



if __name__ == "__main__":
    nodes = Nodes()
    nodes.mainloop()


        