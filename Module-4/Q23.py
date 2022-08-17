"""
 Write a Python class named Rectangle constructed by a length and width
and a method which will compute the area of a rectangle

"""

class rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width
        aofrect=length*width
        print("Area Of Rectangle :",aofrect)
l=int(input("Enter a Length: "))
w=int(input("Enter a Width: "))
r=rectangle(l,w)