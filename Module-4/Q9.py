# Write a Python program to count the number of lines in a text file.
f=open("python.txt","r")
s=len(f.readlines())

print(s)
f.close()