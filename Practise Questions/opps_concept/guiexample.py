import tkinter

screen=tkinter.Tk()

screen.geometry("500x500")
screen.configure(bg="grey")

var_ename_id=tkinter.StringVar()

def myfun():
    print("value of entry= ",var_ename_id.get())
lbl=tkinter.Label(screen,text="Welcome To Tkinter",font=("arial",26,"bold"))
lbl.place(x=10,y=10)

lblname=tkinter.Label(screen,text="Enter Your Name: ",font=("arial",10,"bold"),bg="grey")
lblname.place(x=20,y=80)

e1=tkinter.Entry(screen,textvariable=var_ename_id)
e1.place(x=160,y=80)

btn=tkinter.Button(screen,text="submit",font=("arial",10,"bold"),command=myfun)
btn.place(x=300,y=80)
screen.mainloop()