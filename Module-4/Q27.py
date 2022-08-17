# What is used to check whether an object o is an instance of class A?

#isinstance() function used to check whether an object o is an instance of class A

#eg1 Class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Person:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

emp = Employee("Emma", 11000)
per = Person("sweta", "female")

print(isinstance(emp, Employee))
print(isinstance(per, Employee))

#eg2 Inheritance

class Developer(object):

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Developer:", self.name, "-")

class PythonDeveloper(Developer):

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def display(self):
        print("Python Developer:", self.name, "language:", self.language, "-")


dev = PythonDeveloper("Eric", "Python")
print(isinstance(dev, PythonDeveloper))

print(isinstance(dev, Developer))
