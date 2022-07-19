import re
data='''
      Rakesh is 45 Mahesh is 65 soniya is 86
'''
sname=input("enter a value")
if re.search(sname,data):
    print("yes")
else:
    print("no")
