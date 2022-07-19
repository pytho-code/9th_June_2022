''' Write a python program to sum of the first n positive integers.'''

no=int(input("Enter a number"))

if no>=0:
    for i in range(no):
        no=no+i
    print(no)
else:
    print("Enter Positive Number")
