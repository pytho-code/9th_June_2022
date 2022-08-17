# Write a Python program to count the frequency of words in a file.
f=open("python.txt","r")
s=0
for i in f:
    w=i.split()
    for k in w:
        if k==i:
            s=s+1
print(w,s)