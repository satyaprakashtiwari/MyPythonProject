# __str__  normal work----it must return string only
class MyClass:
    pass

c=MyClass() #c is the reference varaible
print(c) #<__main__.MyClass object at 0x0000015233BA1CC8>

# __str__()  overriding
class C1:
    def __str__(self):
        return "welcome"

c=C1()
print(c) #welcome

class Emp:
    def __init__(self,eid, ename, esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def __str__(self):
        return("EmpID: {} EmpName: {} EmpSalary: {}".format(self.eid,self.ename,self.esal))
        return("Empid: %d Empname: %s Empsal: %g" %(self.eid,self.ename,self.esal))

c=Emp(101,"Satya",20000)
print(c)

#__del__()
class C2:
    def __del__(self):
        print("Destroyed")

c1=C2()  #Destroyed
c2=C2()  #Destroyed

del c1
del c2