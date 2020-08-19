import tkinter as tk
from tkinter import *
import tkinter.messagebox

win = Tk()
win.geometry("600x250+100+100")
win.title("Admin Login")

adminname_var= StringVar()
pass_var = StringVar()

def enter():
	if adminname_var.get() == "sonal" and pass_var.get() == "1234":
		win.destroy()
		import analysis
	else:
		tk.messagebox.showinfo('Error','Authentication Failed')
		adminname_var.set("")
		pass_var.set("")	

def destroy():
	win.destroy()	


adminname_label=Label(win,font = ('arial',18,'bold'),text='Admin name:').pack()
adminname_entrybox=tk.Entry(win,width=30,textvariable=adminname_var).pack()

password_label=Label(win,font = ('arial',18,'bold'),text='Password:').pack()
password_entrybox=tk.Entry(win,width=30,textvariable=pass_var).pack()

enter_btn = Button(win,font = ('arial',12,'bold'), text="Enter", command= enter).pack()
exit_btn = Button(win, padx= 1,font = ('arial',12,'bold'), text="Exit", command= destroy).pack()

win.mainloop()
