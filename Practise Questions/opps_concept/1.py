from tkinter import *

def clicked():
    number.set(number.get()+1)

window = Tk()
window.title("Programme")
window.geometry('350x250')
number = IntVar()

label = Label(window, textvariable=number)
label.grid(column=0,row=0)

button = Button(window, text="Push Me", command=clicked)
button.grid(column=1, row=2)

window.mainloop()