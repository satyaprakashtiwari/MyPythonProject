class MyClass:
    name="tiwari"

    def __init__(self,name):
        print(name)   #constructor argument local
        print(self.name) #accesing class variable

c=MyClass("satya") #satya