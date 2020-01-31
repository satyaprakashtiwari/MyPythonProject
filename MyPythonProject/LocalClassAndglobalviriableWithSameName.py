
a,b=15,25  # global varaible
class MyClass:
    a,b=10,20   # class variable

    def add(self,a,b):  #local variable
        print(a+b)   #accessing local variable
        print(self.a+self.b) #accessing class variable

mc= MyClass()
mc.add(60,40)