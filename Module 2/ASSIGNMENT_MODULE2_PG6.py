'''Write a Python program to sum of three given integers.However, if two
values are equal sum will be zero'''
no1=int(input("Enter a number1"))
no2=int(input("Enter a number2"))
no3=int(input("Enter a number3"))

if no1==no2 or no2==no3 or no3==no1:
    sum=0
    print(sum)
else:
    sum=no1+no2+no3
    print(sum)


