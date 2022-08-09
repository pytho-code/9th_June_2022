from random import random
import tkinter
import random

screen=tkinter.Tk()
screen.title("Rock Paper Scissor")
screen.geometry("500x500")
var_user_choice=tkinter.StringVar()
var_com_choice=tkinter.StringVar()
var_result=tkinter.StringVar()
var_inc_user=tkinter.IntVar()
var_inc_com=tkinter.IntVar()

game_list=["ROCK","PAPER","SCISSOR"]
def myfun(msg):

    var_user_choice.set(msg)
    com=random.choice(game_list)
    var_com_choice.set(com)
    if msg==com:
        var_result.set("Tie")
    else:
        if msg=="ROCK" and com=="PAPER":
            var_result.set("Computer Won")
            var_inc_com.set(var_inc_com.get()+1)
      
        elif  msg=="ROCK" and com=="SCISSOR":
            var_result.set("User Won")
            var_inc_user.set(var_inc_user.get()+1)
       

        elif msg=="PAPER" and com=="SCISSOR":
            var_result.set("Computer Won")
            var_inc_com.set(var_inc_com.get()+1)
      

        
        elif msg=="PAPER" and com=="ROCK":
            var_result.set("User Won")
            var_inc_user.set(var_inc_user.get()+1)
      


        elif msg=="SCISSOR" and com=="ROCK":
            var_result.set("Computer Won")
            var_inc_com.set(var_inc_com.get()+1)
    

        elif msg=="SCISSOR" and com=="PAPER":
            var_result.set("User Won")
            var_inc_user.set(var_inc_user.get()+1)
   

btn=tkinter.Button(text="Rock",font=('arial',20,'bold'),activebackground='black',activeforeground='white',bg='blue',command=lambda:myfun("ROCK"))
btn.place(x=10,y=10)

btn=tkinter.Button(text="Paper",font=('arial',20,'bold'),activebackground='black',activeforeground='white',bg='blue',command=lambda:myfun("PAPER"))
btn.place(x=150,y=10)

btn=tkinter.Button(text="Scissor",font=('arial',20,'bold'),activebackground='black',activeforeground='white',bg='blue',command=lambda:myfun("SCISSOR"))
btn.place(x=300,y=10)

user=tkinter.Label(screen,text="USER",font=('arial',14,'bold'))
user.place(x=10,y=150)

computer=tkinter.Label(screen,text="COMPUTER",font=('arial',14,'bold'))
computer.place(x=10,y=200)


user=tkinter.Label(screen,textvariable=var_user_choice,font=('arial',14,'bold'))
user.place(x=150,y=150)

computer=tkinter.Label(screen,textvariable=var_com_choice,font=('arial',14,'bold'))
computer.place(x=150,y=200)


user=tkinter.Label(screen,textvariable=var_inc_user,font=('arial',14,'bold'))
user.place(x=280,y=150)

computer=tkinter.Label(screen,textvariable=var_inc_com,font=('arial',14,'bold'))
computer.place(x=280,y=200)
'''
user=tkinter.Label(screen,text="Scissor",font=('arial',14,'bold'))
user.place(x=350,y=150)

computer=tkinter.Label(screen,text="Scissor",font=('arial',14,'bold'))
computer.place(x=350    ,y=200)

'''

btn=tkinter.Button(screen,textvariable=var_result,font=('arial',20,'bold'),activebackground='black',activeforeground='white',bg='blue',width=25)
btn.place(x=10,y=400)

screen.mainloop()