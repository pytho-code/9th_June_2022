"""
Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle

"""


class circle:

    def __init__(self,radius):
        self.radius=radius
    
    def area_of_circle(self):
        return(self.radius*self.radius*3.14)
    
    def perimeter_of_circle(self):
        return (2*3.14*self.radius)
    
r=int(input("Enter a Radius: "))
ob=circle(r)
print("Area Of Circle: ",ob.area_of_circle())
print("Perimete Of Circle: ",ob.perimeter_of_circle())