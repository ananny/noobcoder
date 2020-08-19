import tkinter as tk
from tkinter import*

win=tk.Tk()
win.geometry("420x240+200+200")
win.title('The Emotional Buff')

def enter():
	import userlogin
def enter1():
	import analysis




''''C = Canvas(win, bg="white", height=240, width=420)
filename = PhotoImage(file = "D:\\1.png")
background_label = Label(win, image=filename)
background_label.place(x=200, y=200, relwidth=1, relheight=1)

C.pack()'''


label = Label(win, font = ('arial',50,'bold'),text ="Login Page", fg = "steel blue", bd = 10, anchor = 'w').pack()

user_btn = Button(win,font = ('arial',20,'bold'), text="User Login",border='3px', command= enter).pack()

admin_btn = Button(win, font = ('arial',20,'bold'),text="Admin Login", border='3px',command= enter1).pack()

win.mainloop()
