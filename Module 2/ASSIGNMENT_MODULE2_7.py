'''Write a Python program that will return true ifthe two given integervalues
are equal or their sum or difference is 5.'''
from pickle import FALSE, TRUE


no1=int(input("Enter a number1"))
no2=int(input("Enter a number2"))

if no1==no2 or no1+no2==5 or no1-no2==5:
   print(True)
else:
    print(False)