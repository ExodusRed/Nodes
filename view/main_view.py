import tkinter as tk

# from view.diagram import Diagram
from view.component.diagram_view import DiagramView
from view.component.toolbar_view import ToolbarView

class MainView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.root = master
        self.controller = controller

        self.coords = None # should go into diagram

        self.create_ui()

        

        print("MainMenuView Inititalized.")



    def create_ui(self):
        print("Creating UI...")
        

        main_frame = tk.Frame(self.root, bg="black", border=0)
        # toolbar = tk.Frame(main_frame, bg="grey12")

        toolbar_view = ToolbarView(self)
        
        # Toolbar buttons
        add_node_button = tk.Button(
            toolbar_view,
            text="Add Node",
            command=lambda mode="add_node": self.controller.set_mode(mode)
        )

        # self.canvas = tk.Canvas(main_frame, bg="black", width=800, height=600)

        self.diagram = DiagramView(
            master=main_frame,
            width=800,
            height=600,
            bg="black"
        )

        self.diagram.create_grid(100)

        self.coords_label = tk.Label(main_frame, text="(0, 0)")

        # binding

        # self.canvas.bind("<Motion>", self.motion)
        self.diagram.bind("<Motion>", self.motion)


        # Packing on screen

        # main_frame.pack(fill="both") # , anchor="center"
        # toolbar.pack(fill="x")
        # toolbar_view.pack(fill="both", expand=True)
        # add_node_button.pack(pady=10)
        # self.canvas.pack(fill="both")

        # self.diagram.pack(fill="both")
        # self.coords_label.pack(fill="both")

        # start
        
        main_frame.grid(column=0, row=0)
        toolbar_view.grid()
        add_node_button.grid()
        self.diagram.grid()

    def set_mode(self, mode):
        self.controller.set_mode(mode)

    def motion(self, event):
        pass

    def add_node(self):
        pass

    


