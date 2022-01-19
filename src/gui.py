import tkinter as tk
from tkinter import *
class GUI:
    def __init__(self, model):
        self.model = model
        model.PassGUI(self)
    def CreateWindow(self):
        window = tk.Tk()
        window.configure(background='white')
        window.geometry("400x200")
        button = Button(window, text = 'Submit', bg='#ffffff', activebackground='#00ff00')  
        button.pack() 
        window.mainloop()
    def UpdateElevatorLocation(self, location):
        print("Change label to ", location)