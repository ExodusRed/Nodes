class BaseController():
    def __init__(self, view_manager, model):
        self.view_manager = view_manager
        self.model = model
