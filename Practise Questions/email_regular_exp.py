import re
pattern="[a-zA-Z0-9]+@[a-zA-Z]s+\.(com|net|edu)"
email=input("enter")
if re.search(pattern,email):
    print("valid")
else:
    print("invalid")
