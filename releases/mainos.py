from tkinter import *
import os, sys

win = Tk()
win.geometry("500x400")

def appsB():
    os.system("python appsbar.py")

appsBar = Button(win, text="AppsBar", command=appsB)
appsBar.grid(row=0, column=0)

win.mainloop()
