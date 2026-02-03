# import tkinter as tk

# import view.main_menu_view

from view.main_menu_view import MainMenuView
from controller.main_menu_controller import MainMenuController
from model.main_menu_model import MainMenuModel

class ViewManager:
    def __init__(self, root):
        self.root = root

        self.initialize_menu()

    

    # def create_ui(self):
    #     self.main_frame = tk.Frame(self.root)
    #     self.main_frame.pack()

    # def start():

    def initialize_menu(self):
        model = MainMenuModel()
        controller = MainMenuController(self, model)
        view = MainMenuView(self.root, controller)

        view.pack(fill="both")


    def initialize_game(self):
        model = MainMenuModel()
        controller = MainMenuController(self, model)
        view = MainMenuView(self.root, controller)

        view.pack(fill="both")
        