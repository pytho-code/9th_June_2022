class productclass:
    def __init__(self):
        print("Welcome to Product Panel")
        self.mobile=5000
        self.__laptop=4500 #private
    def display(self):
        print(self.mobile)
        print(self.__laptop)
    def updatePrice(self,newlaptopprice):
        self.__laptop=newlaptopprice    