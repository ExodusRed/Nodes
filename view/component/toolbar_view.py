import tkinter as tk

# from algorithm.bfs import BFS


class ToolbarView(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        print("Toolbar initializing...")

        # if master in kwargs

        # algo selector
        # dropdown selector
        # 
        # algo_options = ["default"]
        # algo_options = {"BFS"}
        algo_options = ["BFS"]
        algo_selection = None


        algo_selector = tk.OptionMenu(master=self, variable=algo_selection, value=algo_options[0])
        algo_selection = tk.StringVar(algo_selector)
        algo_selection.set(algo_options[0])
        self.config(width=100, height=100, bg="red")

        start_button = tk.Button(self, text="Start")

        # algo_selector.pack()
        # start_button.pack(fill="both")

        algo_selector.grid()
        start_button.grid()

    class AlgoSelector(tk.Frame):
        def __init__(self, master):
            super().__init__()
        

    
