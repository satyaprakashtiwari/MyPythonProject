class Employee:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def dispemp(self):
        print("EMPID:{}  EMPNAME:{}  ESAL:  {}".format(self.eid,self.ename,self.esal))