"""Write a Python program to count the number of characters (character
frequency) in a string"""
c=0
name=input("enter a name")

for i in range(len(name)):
    if name[i] in name[c]:
       c=c+1
    print(name[i],)
      

