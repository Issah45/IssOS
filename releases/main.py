from tkinter import *
import os, sys

win = Tk()
win.geometry("500x400")
win["bg"] = "#056"

user = Label(win, text="{Insert ProfilePicture Here}", bg=win["bg"], font=("Consolas", 20))
user.pack()

def osOpen():
    os.system("python mainos.py")

signup = Button(win, text="Sign In", font=("Consolas", 14, "bold"), command=osOpen)
signup.pack()

win.mainloop()
