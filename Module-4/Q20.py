#Write python program that user to enter only odd numbers, else will raise an exception
from distutils.log import error


n=int(input("enter no"))
try:
        
    if n%2==0:
        print("ok")

      
except error:
    print("Enter a correct number:")



