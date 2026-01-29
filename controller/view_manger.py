# import tkinter as tk

# import view.main_menu_view

from view.main_menu_view import MainMenuView
from controller.main_menu_controller import MainMenuController
from model.main_menu_model import MainMenuModel

class ViewManager:
    def __init__(self, root):
        self.root = root

        self.start()

    

    # def create_ui(self):
    #     self.main_frame = tk.Frame(self.root)
    #     self.main_frame.pack()

    # def start():

    def start(self):
        main_menu_model = MainMenuModel()
        main_menu_coontroller = MainMenuController(self, MainMenuModel)
        main_menu_view = MainMenuView(self.root, MainMenuController)

        main_menu_view.pack(fill="both")


        