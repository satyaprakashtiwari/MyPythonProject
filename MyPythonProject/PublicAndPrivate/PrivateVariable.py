#private variable can be accessed within class
class MyClass:
    __a=10  #this is perivate variable with __  . Its scope is inside the class

    def disp(self):
        print(self.__a)

o=MyClass()
o.disp() #10

#private method can be accessed within class

class MyClass:
    def __disp1(self):   # this is private method with __.
        print("this is display1 method")

    def disp2(self):
        print("this is display2 method")
        self.__disp1()

c=MyClass()
c.disp2() #this is display2 method
          #this is display1 method
#c.__disp1() #AttributeError: 'MyClass' object has no attribute '__disp1'

#we can use private varaiables outside the class indirectly using methods

class C:
    __empid=101

    def getempid(self,eid):
        self.__empid=eid

    def dispEmpid(self):
        print(self.__empid)

ob=C()
ob.dispEmpid() #101
ob.getempid(104)
ob.dispEmpid() #104  new value be assigned to __empid