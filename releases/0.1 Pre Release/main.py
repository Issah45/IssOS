from tkinter import *

win = Tk()
win.geometry("500x400")
win["bg"] = "#056"

user = Label(win, text="{Insert ProfilePicture Here}", bg=win["bg"], font=("Consolas", 20))
user.pack()

signup = Button(win, text="Sign In", font=("Consolas", 14, "bold"))
signup.pack()

win.mainloop()
