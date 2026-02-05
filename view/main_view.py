import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.root = master
        self.controller = controller

        self.create_ui()

        print("MainMenuView Inititalized.")



    def create_ui(self):
        print("Creating UI...")
        

        main_frame = tk.Frame(self.root, bg="black", border=0)
        main_frame.pack(fill="both") # , anchor="center"

        toolbar = tk.Frame(main_frame, bg="grey12")
        toolbar.pack(fill="x")

        # Toolbar buttons
        add_node_button = tk.Button(toolbar, text="Add Node")

        add_node_button.pack(pady=10)

        self.canvas = tk.Canvas(main_frame, bg="black", width=600, height=800)

        self.canvas.pack(fill="both")





        # start


