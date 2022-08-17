"""
Explain Inheritance in Python with an example? What is init? Or What Is
A Constructor In Python?

It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.



The __init__() function is called automatically every time the class is being used to create a new object.



"""
"""

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis(self):
        print(self.name,self.age)

class student(person):


    def pri(self,year):
        self.year=year
        print(self.name,self.age,self.year)


s=student("sweta",20,2100)"""



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
 def __init__(self,fname,lname,y):
    Person.__init__(self,fname,lname)
    self.y=y

 def wel(self):
    
    print(self.firstname,self.lastname,self.y)

x = Student("sweta","soni",2019)
x.wel()
x.printname()
