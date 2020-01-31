from abc import ABC, abstractmethod

class Cal(ABC):

    def __init__(self,value):
        self.value=value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class C(Cal):
     def add(self):
         print(self.value+100)

     def sub(self):
         print(self.value-10)

cobj=C(100)
cobj.add() #200
cobj.sub() #90