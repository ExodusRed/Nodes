import tkinter as tk

class DiagramView(tk.Canvas):
    def __init__(self, unit=100, **kwargs):
        super().__init__(**kwargs)
        # self.create_grid(unit)
        self.after(50, lambda unit=unit: self.create_grid(unit))

    def create_starting_tile(self, column, row, unit=100):
        starting_tile = self.create_rectangle(
            column,
        )


    def create_grid(self, unit):
        print("Creating grid...")
        self.update_idletasks()
        self.update()


        width, height = self.winfo_width(), self.winfo_height()
        # print(f"width: {width}, height: {height}")

        max_column, max_row = width // unit, height // unit

        print(f"width: {width}, height: {height}")

        self.update_idletasks()
        self.update()

        # self.create_line(0, 100, 300, 100, fill="white")

        for row in range(max_row + 1):
            print(f"row: {row}")
            self.create_line(
                0,
                row * unit,
                width,
                row * unit,
                fill="white"
            )
            print(f"x: , y: {row}")

        for column in range(max_column):
            self.create_line(
                unit * column,
                0,
                unit * column,
                height,
                fill="white"
            )

        self.update_idletasks()