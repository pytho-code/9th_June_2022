import tkinter

screen=tkinter.Tk()

screen.geometry("500x500")
screen.configure(bg="grey")

number=tkinter.IntVar()

def like():
  
    number.set(number.get()+1)

def dislike():
    number.set(number.get()-1)
    
lbl=tkinter.Label(screen,text="Welcome To Tkinter",font=("arial",26,"bold"))
lbl.place(x=50,y=10)

#lblname=tkinter.Label(screen,text=": ",font=("arial",10,"bold"),bg="grey")
#lblname.place(x=20,y=80)



btn=tkinter.Button(screen,text="Like",font=("arial",10,"bold"),height=2,width=20,command=like)
btn.place(x=10,y=80)

btn=tkinter.Button(screen,text="Dis-Like",font=("arial",10,"bold"),height=2,width=20,command=dislike)
btn.place(x=200,y=80)

lblname=tkinter.Label(screen,textvariable=number,font=("arial",10,"bold"),bg="white",width=10)
lblname.place(x=140,y=150)

screen.mainloop()