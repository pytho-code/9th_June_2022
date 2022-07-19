#Write a Python program to get the Factorial number of given number.
fact=int(input("Enter a number"))
for i in range(1,fact):
    fact=fact*i
print(fact)