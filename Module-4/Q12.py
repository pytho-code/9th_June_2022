# Write a Python program to copy the contents of a file to another file.

with open ("python.txt","r") as file1 ,open("copyfile.txt","w") as file2:
    for i in file1:
        file2.write(i)