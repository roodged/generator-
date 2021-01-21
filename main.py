from tkinter import *
from funciones import *
root = Tk()

label = Label(root,text="Generador")
label.pack()

logo = PhotoImage(file = 'logo.gif')
Label(root, image=logo, bd=0).pack()

root.mainloop()