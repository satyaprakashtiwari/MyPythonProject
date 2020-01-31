class MyClass:

    def value(self,val1, val2): #val1 and val2 are local variables
        print(val1)
        print(val2)
        self.val1=val1
        self.val2=val2

    def add(self):
        print(self.val1+self.val2)

mc=MyClass()
mc.value(10,20)
mc.add() #NameError: name 'val1' is not defined    so we need to use self.val1=val1 and self.val1  and val2 vice versa

#with constructor

class MyClass:

    def __init__(self,val1, val2): #val1 and val2 are local variables
        print(val1)
        print(val2)
        self.val1=val1
        self.val2=val2

    def add(self):
        print(self.val1+self.val2)

mc=MyClass(100,200)
mc.add() #NameError: name 'val1' is not defined    so we need to use self.val1=val1 and self.val1  and val2 vice versa