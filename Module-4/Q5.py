# Write a Python program to read last n lines of a file.
f=open("python.txt","r")
n=int(input("Enter a line:"))
for l in (f.readlines()[-n:]):
    print(l)
f.close()