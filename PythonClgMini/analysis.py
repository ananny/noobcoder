import tkinter as tk
from tkinter import*

win = Tk()
win.geometry("650x250+100+100")
win.title("Analysis")

def enter():
	import graph

label = Label(win, font = ('arial',20,'bold'), text ="Which type of movies most people prefer?", fg = "steel blue", bd = 15, anchor = 'w').pack()

a_btn = Button(win,font = ('arial',20,'bold'), text="Data Analysis",border='3px', command= enter).pack()

win.mainloop()
