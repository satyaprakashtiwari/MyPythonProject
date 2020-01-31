class Student:

    def __init__(self,sid,sname,sgrad):
        self.sid=sid
        self.sname=sname
        self.sgrad=sgrad

    def display(self):
        print("Sid: {} Sname: {} Sgrad: {}".format(self.sid,self.sname,self.sgrad))
