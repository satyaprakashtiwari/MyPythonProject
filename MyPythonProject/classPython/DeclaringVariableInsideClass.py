class MyClass:
    a,b=100,200  #class variables

    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)

mc=MyClass()
mc.add() #300
mc.mul() #20000