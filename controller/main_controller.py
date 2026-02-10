from controller.base_controller import BaseController

class MainController(BaseController):
    def __init__(self, view_manager, model):
        # self.view_manager = view_manager
        # self.model = model
        self.mouse_mode = None

        super().__init__(view_manager, model)

        # print("MainMenuContr")

    def set_mode(self, mode):
        if mode == "add_node":
            print("Adding node.")

