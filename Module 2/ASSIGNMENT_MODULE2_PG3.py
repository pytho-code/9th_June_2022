'''Write a Python program to get the Fibonacci series of given range.
0, 1, 1, 2, 3, 5, 8, 13, 21'''
number=int(input("Enter a number"))
s=0
f=1
print(s,f,end=" ")
for i in range(2,number):
   sum=s+f
   print(sum,end=" ")

   s=f
   f=sum


   
