import tkinter as tk
from windowResources.FirstValue import *
from windowResources.PredictionPresentation import *
from windowResources.AlgoTakenPresentation import *
from windowResources.ArchitecturePresentation import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Management Window")
        self.option_add("*header.font", "helvetica 18 bold")
        btn_500_values = tk.Button(self, text="Generate the first 500 values, and graph Yn as a function of Xn")
        btn_architecture = tk.Button(self, text="Takens Algorithm and number of input units")
        btn_learning = tk.Button(self, text="Network learning and number of hidden units")
        btn_prediction = tk.Button(self, text="Predictions")

        self.create_label(name="header", text="HENON SERIES PREDICTION")

        opts = {'padx': 40, 'pady': 5, 'expand': True, 'fill': tk.BOTH}
        btn_500_values.pack(**opts)
        btn_architecture.pack(**opts)
        btn_learning.pack(**opts)
        btn_prediction.pack(**opts)

        btn_500_values.bind("<Button>",
		lambda e: App_win(self))

        btn_prediction.bind("<Button>",
		lambda e: App_prediction(self))

        btn_learning.bind("<Button>",
        lambda e: Presentation(self))

        btn_architecture.bind("<Button>",
		lambda e: App_architect(self))

    def create_label(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)

if __name__ == "__main__":
    app = App()
    app.mainloop()
