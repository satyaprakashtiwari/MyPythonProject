class MyClass:
    def m1(self):   #instance method...........to use need to create object
        print("m1 instance method")

    @staticmethod
    def m2():
        print("m2 static method")

    @staticmethod
    def m3(self):
        print("m3 static method")

mc=MyClass()
mc.m1() #m1 instance method
mc.m2() #m2 static method
MyClass.m2() #m2 static method
MyClass.m3(9) #m3 static method
