

name=input("Enter a Name: ")
Mobile=input("Enter a Mobile Number: ")
Gender=input("Enter a Gender: ")
Age=int(input("Enter a Age: "))
ProductName=input("Enter a Product Name: ")
Qty=int(input("Enter a quantity: "))
CurrentPrice=4829
MakingCharges=589
purchaseamt=CurrentPrice*Qty+MakingCharges
GST=purchaseamt*3/100
dis=int()
pafterdis=int()
if Qty>10:
    
    inamt=MakingCharges*10/100
    MakingCharges=MakingCharges+inamt

if Gender=="Male" and Age<60:
    if purchaseamt>=200000:
        dis=purchaseamt*5/100
        purafterdis=purchaseamt-dis
    elif purchaseamt>=500000:
         dis=purchaseamt*10/100
         purafterdis=purchaseamt-dis
    elif purchaseamt>=1000000:
         dis=purchaseamt*15/100
         purafterdis=purchaseamt-dis 
elif Gender=="Female" and Age<60:
    if purchaseamt>=200000:
        dis=purchaseamt*10/100
        purafterdis=purchaseamt-dis
    elif purchaseamt>=500000:
         dis=purchaseamt*15/100
         purafterdis=purchaseamt-dis
    elif purchaseamt>=1000000:
         dis=purchaseamt*20/100
         purafterdis=purchaseamt-dis
elif Gender=="Male" and Age>=60:
    if purchaseamt>=200000:
        dis=purchaseamt*10/100
        purafterdis=purchaseamt-dis
    elif purchaseamt>=500000:
         dis=purchaseamt*15/100
         purafterdis=purchaseamt-dis
    elif purchaseamt>=1000000:
         dis=purchaseamt*20/100
         purafterdis=purchaseamt-dis
elif Gender=="Female" and Age>=60:
    if purchaseamt>=200000:
        dis=purchaseamt*15/100
        purafterdis=purchaseamt-dis
    elif purchaseamt>=500000:
         dis=purchaseamt*20/100
         purafterdis=purchaseamt-dis
    elif purchaseamt>=1000000:
         dis=purchaseamt*25/100
         purafterdis=purchaseamt-dis
print("---------Invoice---------")
print("Customer Name: ",name)
print("Mobile Number: ",Mobile)
print("Gender: ",Gender)
print("Age : ",Age)
print("Product Name: ",ProductName)
print("Quantity: ",Qty,"Gram")
print("Current Price: ",CurrentPrice, " ( 1 Gram ) " , 4829*Qty)
print("Making Charges: ",MakingCharges)
print("Purchase Amount: ",purchaseamt)
print("------------------------------")
print("Discount Amount: ",dis," Rs")
print("Discount % :",dis/purchaseamt*100," % ")
print("GST :",GST)
print("Net Amount: ",purafterdis+GST)




