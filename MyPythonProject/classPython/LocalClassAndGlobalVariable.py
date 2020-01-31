
i,j=15,25  # global varaible
class MyClass:
    a,b=10,20   # class variable

    def add(self,x,y):  #local variable
        print(x+y)   #accessing local variable
        print(self.a+self.b) #accessing class variable
        print(i+j)  #accessing global variable

mc= MyClass()
mc.add(60,40)