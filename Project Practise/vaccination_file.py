import datetime as dt
import os
d=dt.datetime.now()
format_date=f"{d:%a, %b %d %Y}"

if os.path.exists("/Users/admin/Documents/GitHub/9th_June_2022/Practise Questions/vac_details"):
    print("Folder Exist")
else:
    os.mkdir("/Users/admin/Documents/GitHub/9th_June_2022/Practise Questions/vac_details")


f=open("/Users/admin/Documents/GitHub/9th_June_2022/Practise Questions/vac_details/"+d.strftime("%d %B %Y")+".txt","w")
date=dt.datetime.now()
f.write("Date " +str(date))
first_name=input("Enter a First Name: ")
f.write("\nFirst_Name: "+first_name)
last_name=input("Enter a Last  Name: ")
f.write("\n Last Name: "+last_name)
age=input("Enter an Age: ")
f.write("\n Age: "+str(age))
gender=input("Enter a Gender: ")
f.write("\n Gender: "+gender)
dose=input("Enter a Dose: ")
f.write("\n Dose: "+dose)
f.close()

