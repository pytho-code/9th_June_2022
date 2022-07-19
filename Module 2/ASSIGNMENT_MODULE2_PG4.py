''' Write python program that swap two number with temp variable and
without temp variable.'''
no1=int(input("Enter a no1"))
no2=int(input("Enter a no2"))
print("Number 1:",no1)
print("Number 2:",no2)

temp=no1
no1=no2
no2=temp
print("After Swapping ","Number 1:",no1,"Number 2:",no2)

#second method
no1,no2=no2,no1
print("After Swapping ","Number 1:",no1,"Number 2:",no2)


