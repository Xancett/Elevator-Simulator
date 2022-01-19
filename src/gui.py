import tkinter as tk
from tkinter import *
window = tk.Tk()
window.configure(background='white')
window.geometry("400x200")
button = Button(window, text = 'Submit', bg='#ffffff', activebackground='#00ff00')  
button.pack()  


window.mainloop()