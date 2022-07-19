mobile_store = {}
def menu():
    menu = """
            Menu
      Press 1 for Product Manager
      Press 2 for Customer      
"""

def customer():
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