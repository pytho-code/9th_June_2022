



mobile_store = {}
menu = """
            Menu
      Press 1 for Product Manager
      Press 2 for Customer      
"""
status = True
while status:
    specification = {}
    print(menu)
    role = int(input("Enter a role 1/2"))
    if role == 1:
        print("Product Manager")

        productName = input("Enter a Product Name: ")

        model_num = input("Enter a Model: ")
        color = input("Enter a Color: ")
        qty = int(input("Enter a Quantity: "))
        price = int(input("Enter a Price: "))

        specification["model"] = model_num
        specification["Color"] = color
        specification["Quantity"] = qty
        specification["Price"] = price

        mobile_store[productName] = specification
        print(mobile_store)

    elif role == 2:
        s = True
        cust_product = {}

        while s:
            cart = {}

            print("Customer")
            productName = input("enter a product name: ")
            model_c = input("enter a model number ")
            qty_c = int(input("enter a  Quantity: "))
            if productName in mobile_store.keys():
                    cart["Model"] = model_c
                    cart["Quantycust"] = qty_c
                    totalprice=price*qty
                    cart["Totprice"]=totalprice
                               
                    if qty_c<qty:
                        remainqty=qty-qty_c
                        cart["Remainqty"]=remainqty
                    else:
                        print("Stock is not avilable")   

                    cust_product[productName] = cart
 
                    print(cust_product)
            
                    for v in cust_product.keys():
                        print("-----------------------")
                        print(f"Product : {v}")
                        print("MODEL:" + cust_product[v]["Model"])
                        print("COLOR :" + mobile_store[v]["Color"])
                        print("QUANTITY :" + str(cust_product[v]["Quantycust"]))
                        print("PRICE :" + str(cust_product[v]["Totprice"]))   

            else:

                    print("Product is not available")
            
                    

           
            ch=input("Do you want to purchase more item?: ")
            if ch== 'n' or ch=="no":
                s=False
    

    else:
        print("Invalid Input")

    choice = input("Do you want to continue : Press 'y' for yes 'n' for No : ")
    if choice == "n" or choice == "no":
      '''  specification["model"] = model_num
        specification["Color"] = color
        specification["Remainqty"] = remainqty
        specification["Price"] = price

        mobile_store[productName] = specification
        print(mobile_store)'''
      status = False

for k in mobile_store.keys():
        print("-----------------------")
        print(f"Product : {k}")
        print("MODEL:" + mobile_store[k]["model"])
        print("COLOR :" + mobile_store[k]["Color"])
        print("QUANTITY :" + str(mobile_store[k]["Remainqty"]))
        print("PRICE :" + str(mobile_store[k]["Price"]))

    