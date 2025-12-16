# handles everything to do with presenting

import tkinter as tk

from view.components.diagram import Diagram

class ViewController:
    def __init__(self):
        print("Initializing View Controller.")
        self.views = {}

        self.register_view("main")
        self.load_view("main")
                

    def register_view(self, view_name: str):
        if view_name in self.views:
            return
        # view_class = getattr(view_name.capitalize(), f"view.{view_name}_view")
        # view = view_class(self)


        # self.views[view_name] = view


        module_name = f"view.{view_name}_view"

        try:
            print("try")
            module = __import__(module_name, fromlist=["*"])
        except ModuleNotFoundError as exc:
            raise ImportError(f"Could not import view module.")
        
        candidates = [
            view_name.capitalize() + "View",
            view_name.capitalize()
        ]

        view_class = None

        for cname in candidates:
            view_class = getattr(module, cname, None)
            if isinstance(view_class, type):
                break
                
        if view_class is None:
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and view_name.lower() in name.lower():
                    view_class = obj
                    break

        if view_class is None:
            print("view_class is none.")
            available = [n for n in dir(module) if isinstance(getattr(module, n), type)]
            raise ImportError(f"No view class found in '{module_name}'. Available: {available}")
        
        if view_class is None:
            print("view_class is none.")
        
        if view_class is None:
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and view_name.lower() in name.lower():
                    view_class = obj
                    break

        view = view_class(self)

        self.views[view_name] = view

        print(f"View {view_name} registered.")


    def load_view(self, view_name: str):
        print(f"Loading {view_name}.")
        print(f"Available Views: {self.views}")






        

    # what we need:
    # canvas, toolbar ( for now, additions will follow )

    