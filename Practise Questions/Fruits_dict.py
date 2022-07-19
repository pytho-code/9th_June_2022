fruits={}
menu="""
   press 1 for add fruits
   press 2 for view
   press 3 for purchase
   press 4 for exit
"""

status=True

while status:
    print(menu)
    specification={}
    choice=int(input("enter a choice: "))
    if choice==1:
        fruit_name=input("enter a fruit name: ")
        qty=int(input("enter a quantity: "))
        price=int(input("enter a price: "))

        specification["qty"]=qty
        specification["price"]=price
        fruits[fruit_name]=specification
    elif choice==2:

        for k in fruits.keys():
            print(f"Product name : , {k}")
            print("Fruit qty : ",fruits[k]["qty"])
            print("Fruit price : ",fruits[k]["price"])
    elif choice==3:
        for k in fruits.keys():
            print(f"Product name : , {k}")
            print("Fruit price : ",fruits[k]["price"])


        fruit_name=input("enter a fruit name: ")
        if fruit_name in fruits.keys():
            qty=int(input("enter a quantity: "))
            price=qty*fruits[fruit_name]["price"]

            print("Price ", price)
    elif choice==4:
        status=False
        break        
userchoice=input("do you want to continue?: ")   
if userchoice=='n':
    status=False
else:
    status=True        