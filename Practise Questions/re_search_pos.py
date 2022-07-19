import re

data='''
      Rakesh is 45 Mahesh is 65 Soniya is 86
'''

s=input("enter a value")
print(re.search(s,data))#this will give full expression


for i in re.finditer(s,data):#to get only postion need to use span tag 
    a=i.span()
    print(a)