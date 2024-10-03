from tkinter import * 
import tkinter as tk
from windowResources.PredictionPresentationResources.tab import*
from windowResources.PredictionPresentationResources.tab_3 import*
from windowResources.PredictionPresentationResources.tab_10 import*
from windowResources.PredictionPresentationResources.tab_20 import*
from windowResources.PredictionPresentationResources.courbe_prediction_1 import*
from windowResources.PredictionPresentationResources.courbe_pred_3 import*
from windowResources.PredictionPresentationResources.courbe_pred_10 import*
from windowResources.PredictionPresentationResources.courbe_pred_20 import*

class App_prediction(Toplevel):
    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("Prediction")
        self.option_add("*header.font", "helvetica 18 bold")
        self.create_label(name="header", text="Prediction: ")
        self.geometry("650x400")
        self.resizable(width=0, height=0)

        label_1 = tk.LabelFrame(self, text="prediction one step ahead")
        label_3 = tk.LabelFrame(self, text="prediction three steps ahead")
        label_10 = tk.LabelFrame(self, text="prediction ten steps ahead")
        label_20 = tk.LabelFrame(self, text="prediction twenty steps ahead")
        
        btnCourbe1 = tk.Button(self, text="Plot curve", command=courbe_pred_1)
        btnTab1 = tk.Button(self, text="Show table")

        btnCourbe3 = tk.Button(self, text="Plot curve", command=courbe_pred_3)
        btnTab3 = tk.Button(self, text="Show table")

        btnCourbe10 = tk.Button(self, text="Plot curve", command=courbe_pred_10)
        btnTab10 = tk.Button(self, text="Show table")

        btnCourbe20 = tk.Button(self, text="Plot curve", command=courbe_pred_20)
        btnTab20 = tk.Button(self, text="Show table")

        label_1.place(x=25, y=35, width=600, height=70)
        label_3.place(x=25, y=130, width=600, height=70)
        label_10.place(x=25, y=225, width=600, height=70)
        label_20.place(x=25, y=320, width=600, height=70)

        btnCourbe1.place(x=50, y=60)
        btnTab1.place(x=400, y=60)

        btnCourbe3.place(x=50, y=155)
        btnTab3.place(x=400, y=155 )

        btnCourbe10.place(x=50, y=250)
        btnTab10.place(x=400, y=250)

        btnCourbe20.place(x=50, y=345)
        btnTab20.place(x=400, y=345)

        btnTab1.bind("<Button>",
		lambda e: App_Table(self))

        btnTab3.bind("<Button>",
		lambda e: App_Table_3(self))

        btnTab10.bind("<Button>",
		lambda e: App_Table_10(self))

        btnTab20.bind("<Button>",
		lambda e: App_Table_20(self))
        

    def create_label(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)
