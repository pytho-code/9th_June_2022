eve_list=[]
odd_list=[]
for i in range(1,6):
    number=int(input("entera a number"))

    if number%2==0:
         eve_list.append(number)

    else:
        odd_list.append(number)
        
        
print("odd",odd_list)
print("even",eve_list)
