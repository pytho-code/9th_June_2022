class vehicleclass:
    def speed(self):
        print("speed of vehicle")
class car(vehicleclass):
    def speed(self):
        vehicleclass.speed(self)
        print("160")
class bike(vehicleclass):
    def speed(self):
       vehicleclass.speed(self)
       print("80")
     
car=car()
car.speed()

bike=bike()
bike.speed()