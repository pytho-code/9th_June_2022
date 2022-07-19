pos=0
neg=0
for i in range(1,6):
    n=int(input("enter a number"))
    if n>=0:
        pos+=1
    else:
        neg+=1
print("Pos",pos)
print("Neg",neg)