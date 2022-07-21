#create folder
import os
if os.path.exists("/Users/admin/Documents/GitHub/9th_June_2022/Practise Questions/myfolder"):
    print("Folder Exist")
else:
    os.mkdir("/Users/admin/Documents/GitHub/9th_June_2022/Practise Questions/myfolder")
    print("created folder")