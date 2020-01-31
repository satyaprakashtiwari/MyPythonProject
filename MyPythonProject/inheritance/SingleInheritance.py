class A:
    def m1(self):
        print("method m1 from A")

class B(A):
    def m2(self):
        print("method m2 from B")

a=A()
a.m1() #method m1 from A

b= B()
b.m2() #method m2 from B
b.m1() #method m1 from A

class Parent:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class Child(Parent):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

c=Child()
c.m1() #30
c.m2() #300

p=Parent()
p.m1() #30
