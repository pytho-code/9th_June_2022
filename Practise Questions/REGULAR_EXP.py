import re

data='''
      Rakesh is 45 Mahesh is 65 Soniya is 86
'''

names=re.findall(r"\d{1,3}",data)
age=re.findall(r"[A-Z][a-z]*",data)

mydict={}
c=0
for n in names:
    mydict[n]=age[c]
    c=c+1
for k,v in mydict.items():
    print(f"{k}={v}")    
    