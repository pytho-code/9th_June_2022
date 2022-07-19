Data="""
          Jay Bhavani

          1)Press 1 add to cart
          2)Press 2 remove from a cart
          3)Display all items
          4)Bill Payment

"""
status=True
product=[]
Product_price=[]
Quantity=[]
while status:
    choice=int(input("Enter a choice:"))
    if choice==1:
        No_Of_Item=int(input("Enter No of items"))
        for i in range(No_Of_Item):
            item_name=input("Enter a Product Name:")
            qty=int(input("Enter a Quantiry:"))
            price=int(input("Enter a Price"))
            product.append(item_name)
            Quantity.append(qty)
            Product_price.append(price)
    elif choice==2:
        item_name=input("Enter a Product Name:")

        if item_name in product:
            product.remove(item_name)
            Product_price.remove(price)
        else:
            print("item not exist")
    elif choice==3:
         for i in product:

             print("Product Name: ",i)
             print("price : ",Product_price)
             print("Quantity: ",qty)
    elif choice==4:
        for i in product:
             print("Product Name: ",i)
             print("price : ",Product_price)
             print("Quantity: ",qty)
             total=price*qty
             print("Total Payment: ",total)

        
    else:
            print("Wrong Choice")
    user_choice=input("Do yo want to add any more Operations type 'y' or'Y and 'N' or 'n'")
    if user_choice=='N' or user_choice=='n':
        status =False 
    else:
        status=True


        
        