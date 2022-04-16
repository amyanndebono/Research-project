from tkinter import *

from matplotlib.pyplot import show

root = Tk()
root.title('Covid regulations')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = ["Malta", "Italy", "Germany", "France", "Austria", 
"England", "Spain", "Portugal", "Switzerland","Poland"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options )
drop.pack()

showButton = Button(root, text="Show Covid Regulations", command=show).pack()

my_text = Text(root, width=60, height=20, font=("calibri", 12))
my_text.pack(pady = 20)

root.mainloop()
