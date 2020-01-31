class Emp:
    def __init__(self,eid, ename, esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def display(self):
        print("EmpID: {} EmpName: {} EmpSalary: {}".format(self.eid,self.ename,self.esal))
        print("Empid: %d Empname: %s Empsal: %g" %(self.eid,self.ename,self.esal))

c=Emp(101,"Satya",20000)
c.display() #EmpID: 101 EmpName: Satya EmpSalary: 20000
            #Empid: 101 Empname: Satya Empsal: 20000