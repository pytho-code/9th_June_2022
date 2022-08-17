# Write a Python program to read a file line by line and store it into a list
f=open("python.txt","r")
lst=f.readlines()
print(lst)
f.close()