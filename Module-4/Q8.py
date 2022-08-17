# Write a python program to find the longest words.

f=open("python.txt","r")
str = f.read()
words = str.split()
max_len = len(max(words,key=len))
print(max_len)
for word in words:
    if len(word)==max_len:
        longest_word =word
         
print(longest_word)