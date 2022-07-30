import fac,stu

f=fac.facultyclass()
s=stu.studentclass()
lst="""
    1.Faculty
    2.Student
"""
s=True
while s:



    print(lst)
    ch=int(input("enter your choice"))
    if ch==1:
        status=True
        while status:
            name=input("Enter a name: ")
            email=input("Enter a email: ")
            number=input("Enter a number: ")
            sub=input("Enter a sub: ")
            city=input("Enter a city: ")
            f.createfaculty(name,email,number,sub,city)

            choice=input("do ypu wnat to continue 'y' 'n")
            if choice=="y":
                status=True
            else:
                status=False     
    elif ch==2:
            status=True
            while status:
                name=input("Enter a name: ")
                email=input("Enter a email: ")
                city=input("Enter a city: ")
                marks=input("Enter a marks: ")
                contact=input("Enter a contact: ")
                fees=input("Enter a fees: ")
                sub=input("Enter a subject: ")
                s.createstudent(name,email,city,marks,contact,fees,sub)

            choice=input("do ypu wnat to continue 'y' 'n")
            if choice=="y":
                status=True
            else:
                status=False     

opt=input("Do you want to continue adding the data? ")
if opt=="y":
    s=True
else:
    s=False