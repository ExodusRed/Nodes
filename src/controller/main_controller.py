from controller.view_controller import ViewController

# Main controller handles all controllers

class MainController():
    def __init__(self):
        print("Initializing Main Controller.")
        self.view_controller = ViewController()

        # on launch:
        # load or create save_file
        # create diagram ( canvas )
        # load presets / preferences or standard preferences | optional (kimfl)
        # draw nodes and edges

        

