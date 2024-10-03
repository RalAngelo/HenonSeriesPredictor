from tkinter import * 
import tkinter as tk
import numpy as np
from windowResources.ArchitecturePresentationResources.codeResources.apprentissage_2 import*

class App231(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Learning")
        self.geometry("700x700")
        self.option_add("*header.font", "helvetica 18 bold")
        self.create_label(name="header", text="Learning: ")

        label231 = tk.LabelFrame(self, text="Architecture Information (2,3,1)")
        label231.place(x=50, y=50, width=600, height=400)

        labelPoid = tk.LabelFrame(self, text="Weights for the minimal NMSE")
        labelPoid.place(x=50, y=460, width=400, height=200)

        v=Scrollbar(label231, orient='vertical')
        v.pack(side=RIGHT, fill='y')

        T = Text(label231, width=590, height=490, yscrollcommand=v.set)
        v.config(command=T.yview)
        T.pack()

        v2=Scrollbar(labelPoid, orient='vertical')
        v2.pack(side=RIGHT, fill='y')

        T2 = Text(labelPoid, width=390, height=190, yscrollcommand=v2.set)
        v2.config(command=T2.yview)
        T2.pack()

        def affichage():
            for i in range(9):
                fact1 = ("""************ """+"""EPOCH"""+str(i+1)+ """ ************""" + """\n""" +
                """ NMSE of epoch """ + str(i+1) + """: """+ """\"""" + str(a3[i])+ """\"""" + 
                """\n""" 
                + """the weights obtained between the input layer and the hidden layer: """ +
                """\n"""
                )

                affiche_poid_2 = np.zeros((3, 2))
                affiche_poid_3 = np.zeros((1, 3))
                for x in range(3):
                    for y in range(2):
                        affiche_poid_2[x, y] = b3[i, x, y]
                for x in range(1):
                    for y in range(3):
                        affiche_poid_3[x, y] = c3[i, x, y]
                
                fact2 = (str(affiche_poid_2) + """\n"""
                + """the weights obtained between the hidden layer and the output layer: """ + """\n"""
                + str(affiche_poid_3) + """\n""" + """\n"""
                )

                T.insert(END, fact1 + fact2)
            
        def affichagePoids():
            fact1 = ("""Minimal NMSE: """ + str(np.min(a3)) + """\n""")
            fact2 = ("""the corresponding weights are: """ + """\n""")
            affiche_2 = np.zeros((3, 2))
            affiche_3 = np.zeros((1, 3))
            for x in range(3):
                for y in range(2):
                    affiche_2[x, y] = b3[np.where(a3 == np.min(a3))[0], x, y]
            for x in range(1):
                for y in range(3):
                    affiche_3[x, y] = c3[np.where(a3 == np.min(a3))[0], x, y]
            
            fact3 = ("""the weights obtained between the input layer and the hidden layer: """ + 
            """\n""" + str(affiche_2) + """\n""" 
            + """the weights obtained between the hidden layer and the output layer: """ + """\n"""
            + str(affiche_3) + """\n"""
            )

            T2.insert(END, fact1+fact2+fact3)

        bouton221 = tk.Button(self, text="Architecture Information", command=affichage)
        bouton221.place(x=455, y=510)

        boutonPoid = tk.Button(self, text="weights", command=affichagePoids)
        boutonPoid.place(x=455, y=550)

        boutonCourbe = tk.Button(self, text="curve", command=courbe_nmse_3)
        boutonCourbe.place(x=455, y=590)

    
    def create_label(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)
