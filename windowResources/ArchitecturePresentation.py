from tkinter import *
import tkinter as tk
# Importing the windows to display
from windowResources.ArchitecturePresentationResources.presentation_1 import *
from windowResources.ArchitecturePresentationResources.presentation_2 import *
from windowResources.ArchitecturePresentationResources.presentation_3 import * 

class Presentation(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title('Network Learning')
        
        # Style option for text
        self.option_add("*header.font", "helvetica 18 bold")

        # List of option buttons for learning
        bouttonPresentation1 = tk.Button(self, text="Architecture Presentation (2,1,1)")
        bouttonPresentation2 = tk.Button(self, text="Architecture Presentation (2,2,1)")
        bouttonPresentation3 = tk.Button(self, text="Architecture Presentation (2,3,1)")

        # Placement of the title
        self.createLabel(name="header", text="Learning Options")

        # Placement of the buttons
        opts = {'padx': 40, 'pady': 5, 'expand': True, 'fill': tk.BOTH}

        bouttonPresentation1.pack(**opts)
        bouttonPresentation2.pack(**opts)
        bouttonPresentation3.pack(**opts)

        # Call the presentations
        bouttonPresentation1.bind("<Button>", 
        lambda e: App_211(self))

        bouttonPresentation2.bind("<Button>", 
        lambda e: App221(self))

        bouttonPresentation3.bind("<Button>", 
        lambda e: App231(self)) 

    def createLabel(self, **options):
        tk.Label(self, **options).pack(padx=20, pady=5, anchor=tk.W)
