'''
 Write a Python program to append text to a file and display the text.

'''

f=open("python.txt","a")
f.write("shanay")

f.close()

f=open("python.txt","r")
print(f.read())
f.close()

