list_uniq=[]
print(list_uniq)

c=1
s=True
while s:
    number=int(input("Enter a number"))
    if c<=12:
       if number not in list_uniq:
        list_uniq.append(number)
        c+=1
       else:
        pass
    else:
        s=False
print(list_uniq)

