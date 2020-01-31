class MyClass:

    def m1(self):
        print("this is method m1")
        self.m2(100)

    def m2(self,a):
        print("this is method m2",a)

mc=MyClass()
mc.m1() #this is method m1
        #this is method m2 100