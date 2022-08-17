from abc import ABC,abstractmethod
#ABC:Abstarct Base Class

"""
abstact method:which contain only method declaration no body
 
 this kind of method does not contain method defination

"""
class RBI(ABC):
    @abstractmethod
    def roi(self):
        #method declaration only
        pass

class SBI(RBI):
    def roi(self):
        print("6.5")

class HDFC(RBI):
    def roi(self):
        print("8.5")

sbi=SBI()
hdfc=HDFC()

sbi.roi()
hdfc.roi()

