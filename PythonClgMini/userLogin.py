from tkinter import*
import tkinter as tk
win = Tk()

win.geometry("600x450+100+100")
win.title("User Login")


def enter():
	import temp2

label = Label(win, font = ('arial',50,'bold'), text ="WELCOME!!", fg = "steel blue", bd = 10, anchor = 'w').pack()
label1 = Label(win, font = ('arial',40,'bold'), text ="The Emotional Buff", fg = "red", bd = 10, anchor = 'w').pack()

name_label=Label(win,font = ('arial',18,'bold'),text='Name:').pack()
name_var=tk.StringVar()
name_entrybox=tk.Entry(win,width=30,textvariable=name_var).pack()

email_label=Label(win,font = ('arial',18,'bold'),text='Email-id:').pack()
email_var=tk.StringVar()
email_entrybox=tk.Entry(win,width=30,textvariable=email_var).pack()

mobile_label=Label(win,font = ('arial',18,'bold'),text='Mobile-no:').pack()
mobile_var=tk.StringVar()
mobile_entrybox=tk.Entry(win,width=30,textvariable=mobile_var).pack()

def action():
    username=name_var.get()
    useremail=email_var.get()
    usermobile=mobile_var.get()
    print(f'{username}')
    print(f'{useremail}')
    print(f'{usermobile}')
    
    with open('file.txt','a') as f:
        f.write(f'{username},{useremail},{usermobile}')


save_but=Button(win,font = ('arial',15,'bold'), text="Save",bg="steel blue",border='3px',command= action).pack()
submit_but=Button(win,font = ('arial',15,'bold'), text="Submit",bg="steel blue",border='3px',command= enter).pack()

win.mainloop()
